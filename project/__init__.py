from fastapi import APIRouter
from typing import List, Optional
from enum import Enum

app01 = APIRouter()


@app01.get("/path/parameters")
async def path_parameters():
    return {"param1": "value1", "param2": "new GET"}


@app01.get("/path/{parameters}")
async def path_parameters(parameters: str):
    return {"value": "value", "params": parameters}


class CityName(str, Enum):
    Beijing = "Beijing time"
    Shanghai = "Shanghai time"


@app01.get("/enum/{city}")
async def list_city(city: CityName, confirmed: Optional[int] = None, deaths: Optional[int] = None):
    if city == CityName.Beijing:
        return {"city_name": city, "confirmed": confirmed, "deaths": deaths}
    elif city == CityName.Shanghai:
        return {"city_name": city, "confirmed": confirmed, "deaths": deaths}
    else:
        return {"code": 400, "message": "Error Message in City data"}


@app01.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return f"file path: {file_path}"
