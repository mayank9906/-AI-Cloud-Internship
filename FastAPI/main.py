from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from datetime import datetime

# ----------------------------------------
# Logging Configuration
# ----------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# ----------------------------------------
# FastAPI App
# ----------------------------------------

app = FastAPI(title="Student Management API")

# ----------------------------------------
# Temporary Storage
# ----------------------------------------

students = []

# ----------------------------------------
# Student Model
# ----------------------------------------

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# ----------------------------------------
# Health Check
# ----------------------------------------

@app.get("/health")
def health():

    logger.info("Health endpoint accessed.")

    return {
        "status": "Healthy",
        "service": "Student API",
        "timestamp": datetime.now()
    }

# ----------------------------------------
# Add Student
# ----------------------------------------

@app.post("/students")
def add_student(student: Student):

    try:

        # Check Duplicate ID

        for s in students:
            if s.id == student.id:
                raise HTTPException(
                    status_code=400,
                    detail="Student ID already exists."
                )

        students.append(student)

        logger.info(f"Student Added : {student.name}")

        return {
            "message": "Student added successfully.",
            "student": student
        }

    except HTTPException:
        raise

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

# ----------------------------------------
# Get All Students
# ----------------------------------------

@app.get("/students")
def get_students():

    logger.info("Viewing all students.")

    return students

# ----------------------------------------
# Get Student by ID
# ----------------------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student.id == student_id:

            logger.info(f"Student Found : {student.name}")

            return student

    raise HTTPException(
        status_code=404,
        detail="Student Not Found."
    )

# ----------------------------------------
# Delete Student
# ----------------------------------------

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:

            deleted_student = students.pop(index)

            logger.info(f"Deleted : {deleted_student.name}")

            return {
                "message": "Student deleted successfully."
            }

    raise HTTPException(
        status_code=404,
        detail="Student Not Found."
    )
