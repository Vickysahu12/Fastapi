from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

#multuiple body parameters
# how to add pydantic field into our code:
class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        description = "about of the product",
        max_length=100,
        min_length=3
    )
    price: float = Field(
        gt=0,
        title="product price"
    )
    stock: int | None = None

# class Seller(BaseModel):
#     username:str
#     fullname:str | None = None

# @app.post("/product")
# async def create_product(product:Product, seller:Seller):
#     return{"product":product, "seller":seller}
    

# Netsted body models 

