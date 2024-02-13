from fastapi import APIRouter, Form
from pydantic import BaseModel
from typing import Optional

app02 = APIRouter()


# @app.get("/login/")
# async def login(*, username: str = Form(...), password: int = Form(...)):
#     return {"username": username, "password": password}


class CityInfo(BaseModel):
    province: str
    country: str
    is_true: Optional[bool] = None


@app02.get('/')
async def index():
    return {'message': 'Hello World'}


@app02.get("/city/{city}")
async def city(city: str, query_string: Optional[str] = None):
    return {'city': city, 'query_string': query_string}


@app02.put("/city/{city}")
async def city(city: str, city_info: CityInfo):
    return {'city': city, 'city_info': city_info, 'is_true': city_info.is_true} 
