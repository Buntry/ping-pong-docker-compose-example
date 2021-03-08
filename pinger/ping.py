from fastapi import FastAPI
from datetime import datetime
import requests
import json

app = FastAPI()

@app.get("/ping")
async def ping():
    res = requests.get("http://ponger:8000/pong")
    data = json.loads(res.content)
    then = datetime.strptime(data["t"], "%Y-%m-%d %H:%M:%S.%f")
    ms = round((datetime.now() - then).total_seconds() * 1000, 2)
    return { "ponged": f"{ms}ms" }
    