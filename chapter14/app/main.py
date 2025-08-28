from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id:int
    name:str
    price:float
    stock: int | None = None

# Without return type annotation
# @app.get("/")
# async def main():
#     return{"kuch bhi yahan return kar sakte hai because it dont have any return type annotartion"}

# with return type annotation
# @app.get("/products/")
# async def get_product() -> Product:
#     return {"id":1, "name":"aiml course","price":12000.50,"stock":23}

class BaseUser(BaseModel):
    username:str
    fullname:str | None = None

class UserIn(BaseUser):
    password:str

@app.get("/products/")
async def get_product() -> List[Product]:
    return  [
        {"id":1, "name":"aiml course","price":12000.50,"stock":23},
        {"id":3, "name":"python course","price":1200.50,"stock":23}
        ]

# post request return type annotation :
@app.post("/productdetails/")
async def all_prod(product:Product) -> Product:
    return product

@app.post("/user/")
async def create_user(user:UserIn) -> BaseUser:
    return user