import uvicorn
from fastapi import FastAPI, Response
from pathlib import Path
from mongo_utils import get_dbs
from models.student import Student

app = FastAPI()

@app.get("/")
async def root():
    return Response(content=Path('demo_image.png').read_bytes(), media_type='image/png')


@app.post('/add_student')
async def add_student(student: Student):
    return 'OK'

@app.get('/dbs')
async def dbs():
    return get_dbs()


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, log_config='log.ini')
