from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import time

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


@app.get("/health")
async def health():
    return {"unix_time": time.time()}
