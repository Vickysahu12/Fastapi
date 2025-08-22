from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# this is without pydantic
# @app.get("/product")
# async def create_prod(new_product:dict):
#     return new_product

# with pydantic
# define the product model in pydantic
class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

# @app.post("/product")
# async def create_prod(new_product:Product):
#     return new_product

# how to access atribute inside the function :
# @app.post("/product")
# async def create_prod(new_product:Product):
#     print(new_product.id)
#     print(new_product.name)
#     print(new_product.price)
#     print(new_product.stock)
#     return new_product

# how we can add new calculated attribute
@app.post("/product")
async def create_prod(new_prod:Product):
    prod_dict = new_prod.model_dump()
    prod_with_tax = new_prod.price + (new_prod.price * 18 / 100)
    prod_dict.update({"price with tax":prod_with_tax})
    return prod_dict

# combining request body with paramenetrs
@app.put("/product/{product_id}")
async def update_prod(product_id:int, new_updated_product:Product):
    return{"product_id":product_id, "new_updated_product":new_updated_product}

# combining request body with path paramenetrs
@app.put("/product/{product_id}")
async def update_prod(product_id:int, new_updated_product:Product, discount: float | None = None):
    return{"product_id":product_id, "new_updated_product":new_updated_product, "discount":discount}