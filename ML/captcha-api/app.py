import fastapi
from fastapi import Request
from fastapi.responses import HTMLResponse
from core.api import api_route
from fastapi.staticfiles import StaticFiles


app = fastapi.FastAPI()

app.include_router(api_route)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def main_root(request: Request):
    return "<a href='/api/image-captcha'>show random captcha</a>"