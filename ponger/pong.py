from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/pong")
async def pong():
    return { "t": f"{datetime.utcnow()}" }
