from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

# import jinja template
from fastapi.templating import Jinja2Templates
import time

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.j2",
        {
            "request": request,
            "title": "FastAPI Jinja2 Template Example",
            "heading": "FastAPI Jinja2 Template Example",
            "content": "This is a simple example of using Jinja2 templates with FastAPI.",
        },
    )


@app.get("/health")
async def health():
    return {"unix_time": time.time()}


@app.get("/healthz")
async def healthz():
    return {"unix_time": time.time()}
