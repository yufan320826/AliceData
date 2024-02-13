import uvicorn
from fastapi import FastAPI
from project import app01
from project.main import app02
from SHOP.SHOP_INFO import SHOP
from USER.user import USER
from uploadfile import PDF
from tortoise.contrib.fastapi import register_tortoise
from config import db

app = FastAPI()

register_tortoise(
    app=app,  # 注册的app
    config=db.FastAPI_TO_ORM,  # 数据库配置
    # generate_schemas=True,  # 生成schema | 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 添加异常处理 | 生产环境不要开，会泄露调试信息
)

app.include_router(app01, prefix='/type', tags=['城市检查'])
app.include_router(app02, prefix='/main', tags=['适应'])
app.include_router(USER, prefix='/ShopUser', tags=['用户'])
app.include_router(SHOP, prefix='/Shop', tags=['商品'])
app.include_router(PDF, prefix='/PDF', tags=['文件上传'])

if __name__ == '__main__':
    uvicorn.run('run:app', host='127.0.0.1', port=9000, reload=True, workers=12)
    # reload 动态修改 | workers 进程数
    # fastapi 高性能的web服务
    # asyncio | await
