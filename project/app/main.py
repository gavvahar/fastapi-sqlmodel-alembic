from fastapi import FastAPI

from app.db import init_db
from app.models import Song

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
