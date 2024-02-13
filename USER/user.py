from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse
from tortoise.contrib.pydantic import pydantic_model_creator
from db.models import *

USER = APIRouter()

security = HTTPBasic()


# @USER.get("/user/userinfo")
# async def UserInfo(id: int, username: str, leval: int, active: bool, creat_time: str, uid: int):
#     user = UserINNO(id=id, username=username, leval=leval, active=active, creat_time=creat_time, uid=uid)
#     if user.active == True:
#         return {
#             "username": user.username,
#             "leval": user.leval,
#             "creat_time": user.creat_time,
#             "uid": user.uid
#         }
#     else:
#         return {"active": False}


# 用户登录认证
# @USER.get("/user/login")
# async def Userindex(credentials: HTTPBasicCredentials = Depends(security)):
#     username = credentials.username
#     password = credentials.password
#     if username == "root" and password == "qwer1234":
#         data = {"username": username, password: password}
#         return {"code": 200, "msg": "登录成功", data: data}
#     else:
#         return {"code": 400, "msg": "用户名或密码错误"}


# 测试用户模型
class UserRegisterRequest(BaseModel):
    username: str
    email: str
    age: Optional[int]
    birthday: Optional[str]
    password: str


# 测试用户详情
class UserInfoRequest(BaseModel):
    bio: str
    address: Optional[str] = None
    school: Optional[str] = None
    user: int


# 定义相应模型
UserResponse = pydantic_model_creator(User)
UserInfoResponse = pydantic_model_creator(UserDetail)


# 注册用户
@USER.post("/user/register", response_model=UserResponse)
async def UserRegister(user: UserRegisterRequest):
    user = await User.create(
        name=user.username,
        email=user.email,
        age=user.age,
        birthday=user.birthday,
        password=user.password,
        url=user.user_scl
    )

    return await UserResponse.from_tortoise_orm(user)


# 查看所有用户{id/username}
@USER.get("/user/getall")
async def UserGet():
    data = await User.all()
    return {"code": 200, "data": data}


# 用户登录
@USER.post("/user/login")
async def UserLogin(user: UserRegisterRequest):
    user = await User.get(name=user.username, password=user.password)
    if not user:
        return {"code": 400, "msg": "用户名或密码错误"}
    else:
        return {"code": 200, "msg": "登录成功"}


# 查看用户
@USER.get("/user/getuser/{user_id}", response_model=UserResponse)
async def UserGET(user_id: int):
    user_data = await User.get(id=user_id)
    if not user_data:
        return {"code": 400, "msg": "暂无用户信息"}
    else:
        return await UserResponse.from_tortoise_orm(user_data)


# 创建用户详情
@USER.post("/userinfo/register", response_model=UserInfoResponse)
async def UserInfoCreate(userinfo: UserInfoRequest):
    userinfo = await UserDetail.create(
        bio=userinfo.bio,
        address=userinfo.address,
        school=userinfo.school,
        user=userinfo.user
    )

    return await UserInfoResponse.from_tortoise_orm(userinfo)


# 查看用户详情
@USER.get("/userinfo/get/{user_id}", response_model=UserInfoResponse)
async def UserInfoUpdate(user_id: int):
    userinfo = await UserDetail.get(user=user_id)
    if not userinfo:
        return {"code": 400, "msg": "暂无用户详情"}
    else:
        return await UserInfoResponse.from_tortoise_orm(userinfo)
