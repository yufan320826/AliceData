from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Optional
from fastapi import Request

SHOP = APIRouter()


class ShopInfo(BaseModel):
    shop_name: str
    shop_type: str = "正在营业"
    shop_address: str = "大润发国际有限公司"
    shop_phone: int = 100114811
    is_active: Optional[bool] = True


class BeadInfo(BaseModel):
    bead_name: str
    bead_type: str
    bead_time: str
    bead_price: int


@SHOP.post("/shop/Bead")
async def shop_bead(bead: BeadInfo, user: Optional[str] = None):
    if user != "json":
        return {f"您购买的是{bead.bead_name},价格是{bead.bead_price},烘培时间是{bead.bead_time},未过期{bead.bead_type}"}
    else:
        return {"您已经被拉入黑名单,请前往最近的派出所解除"}


@SHOP.get("/shop/supermarket")
async def shop_supermarket(supermarket: ShopInfo):
    if supermarket.is_active == True:
        return {'msg': "该商场正在营业"}
    else:
        return {'msg': "该商场未营业"}


@SHOP.get("/shop/shopinfo")
async def shop_info(shop: ShopInfo):
    return f"名称是{shop.shop_name},地址是{shop.shop_address},电话是{shop.shop_phone},是否营业{shop.is_active}"


"测试可选参数 Query(None,*) | 必选参数 Query(...,*)"


@SHOP.post("/shop/shopname")
async def shop_name(shop: ShopInfo = None, q: str = Query(None, max_length=10)):
    result = {"shop_name": shop.shop_name, "shop_address": shop.shop_address, "shop_phone": shop.shop_phone,
              "is_active": shop.is_active}
    if q:
        result.update({"q": q})
    else:
        return {'code': 400, 'msg': '请传入查询参数'}
    return result


@SHOP.post("/shop/shopNone")
async def shop_name(shop: ShopInfo = None, q: str = Query(..., max_length=10)):
    result = {"shop_name": shop.shop_name, "shop_address": shop.shop_address, "shop_phone": shop.shop_phone,
              "is_active": shop.is_active}
    if q:
        result.update({"q": q})
    else:
        return {'code': 400, 'msg': '请传入查询参数'}
    return result


@SHOP.get("/shop/ShopCar/{shop_car_id}")
async def shop_car(user_shop: str,
                   request: Request):
    data = {}
    data["shop_car_id"] = user_shop
    data["headers"] = request.headers
    data["host"] = request.client.host
    data["URL"] = request.url
    data["name"] = request.query_params.get("name")
    data["age"] = request.query_params.get("age")
    data["area"] = request.query_params.get("area")

    return {"code": 200, "data": data, 'msg': "SUCCESS"}



