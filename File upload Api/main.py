from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import shutil
import logging
import psycopg2

# -----------------------------
# Logging
# -----------------------------
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(title="File Upload API")
connection = psycopg2.connect(
    host="localhost",
    database="legalai",
    user="postgres",
    password="root"
)

cursor = connection.cursor()

# -----------------------------
# Upload Folder
# -----------------------------
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():

    return {
        "status": "Healthy",
        "service": "File Upload API"
    }

# -----------------------------
# Upload Document
# -----------------------------
@app.post("/documents")
def upload_document(file: UploadFile = File(...)):

    allowed_extensions = [".pdf", ".docx"]

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
     

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save metadata to PostgreSQL
    cursor.execute(
        """
        INSERT INTO documents (filename, filepath, filetype)
        VALUES (%s, %s, %s)
        """,
        (
            file.filename,
            file_path,
            file.content_type
        )
    )

    connection.commit()

    logger.info(f"{file.filename} uploaded successfully.")

    return {
        "message": "File Uploaded Successfully",
        "filename": file.filename,
        "content_type": file.content_type,
        "location": file_path
    }

   
