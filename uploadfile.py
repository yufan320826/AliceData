from fastapi import APIRouter, File, UploadFile, Response
from typing import List

PDF = APIRouter()


@PDF.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        f.write(await file.read())
    return {"code": 200, "msg": "上传成功"}


"多个文件上传"


@PDF.post("/uploadfile/jpg")
async def upload_file_jpg(files: List[UploadFile] = File(...)):
    """
    :param files:
    :return: SUCCESS
    :data success_files
    """
    success_files = []
    for file in files:
        if file.filename == "Saber.jpg":
            file.filename = "Arthur.jpgdddd"
        with open(file.filename, "wb") as f:
            f.write(await file.read())
            success_files.append(file.filename)

    return {"code": 200, "msg": f"已上传成功文件:{success_files}"}


"""
:return JPG
"""


@PDF.get("/uploadfile/saber")
async def upload_file_jpg():
    with open("D:\dowload\Saber.jpg", "rb") as f:
        data = f.read()
        return Response(data, media_type="image/jpeg")
