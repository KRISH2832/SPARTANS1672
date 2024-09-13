import fastapi
from fastapi.responses import JSONResponse
from fastapi import Request
import os
from random import randint

api_route = fastapi.APIRouter(prefix="/api")
img_data = os.listdir("./static/train/")
length = len(img_data)

@api_route.get("/ping", response_class=JSONResponse)
async def ping(request: Request):
    return {"response": "pong"}

@api_route.get("/image-captcha", response_class=JSONResponse)
async def camlin(request: Request):
    rand = randint(0, length-1)
    verify = img_data[rand].split("_")[0]
    return {"image": "/static/train/" + img_data[rand], "verify": verify}