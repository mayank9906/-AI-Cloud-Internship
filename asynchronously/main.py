from fastapi import FastAPI, UploadFile, File, BackgroundTasks
import os
import shutil
import time

app = FastAPI(title="Background Processing API")

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def process_file(filename):
    print(f"Processing {filename}...")

    # Simulate processing
    time.sleep(5)

    source = os.path.join(UPLOAD_FOLDER, filename)
    destination = os.path.join(PROCESSED_FOLDER, filename)

    shutil.move(source, destination)

    print(f"{filename} Processed Successfully!")


@app.post("/upload")
def upload_file(background_tasks: BackgroundTasks,
                file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    background_tasks.add_task(process_file, file.filename)

    return {
        "message": "File Uploaded.",
        "status": "Processing Started",
        "filename": file.filename
    }


@app.get("/health")
def health():
    return {"status": "Healthy"}
