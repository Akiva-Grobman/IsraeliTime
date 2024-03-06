import uvicorn
from fastapi import FastAPI, Response
from pathlib import Path

app = FastAPI()

@app.get("/")
async def root():
    return Response(content=Path('demo_image.png').read_bytes(), media_type='image/png')


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, log_config='log.ini')
