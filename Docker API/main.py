from fastapi import FastAPI, UploadFile, File, BackgroundTasks
import os
import shutil
import time
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME"))

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

PROCESS_TIME = int(os.getenv("PROCESS_TIME", 5))


def process_file(filename: str):
    print(f"Processing {filename}...")

    time.sleep(PROCESS_TIME)

    source = os.path.join(UPLOAD_FOLDER, filename)
    destination = os.path.join(PROCESSED_FOLDER, filename)

    shutil.move(source, destination)

    print(f"{filename} processed successfully.")


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.post("/upload")
def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    background_tasks.add_task(process_file, file.filename)

    return {
        "message": "File uploaded successfully.",
        "status": "Background Processing Started"
    }
