import uvicorn
from typing import Optional
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from mongo_utils import get_dbs, add_student_to_db, get_students_from_db
from models.student import Student, StudentLogin, Student
from config import Config

# app = FastAPI(docs_url=None, redoc_url=None)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
@app.get("/favicon.ico")
async def root():
    return Response(content=Path('demo_image.png').read_bytes(), media_type='image/png')


@app.post('/add_student')
async def add_student(student: StudentLogin):
    student = Student(**student.model_dump())
    add_student_to_db(student.model_dump())
    return 200

@app.get('/students')
async def get_students(token: str = '') -> list[Student]:
    if token == Config.student_token:
        return [Student(**r) for r in get_students_from_db()]
    print(f'Invalid token - {token}')
    return []

@app.post('/testing')
async def test(dummy: dict):
    return 200

@app.get('/dbs')
async def dbs():    
    return get_dbs()


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, log_config='log.ini')
    # uvicorn.run("main:app", host='127.0.0.1', port=8080)
