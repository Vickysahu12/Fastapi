from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Nested body models
# class Category(BaseModel):
#     name: str = Field(
#         title="category name",
#         description="The name of the AI Product",
#         max_length=50,
#         min_length=3

#     ),
#     description: str | None = Field(
#         title="category name",
#         description="a brief description of the AI Product",
#         max_length=250,
#     )

# class Product(BaseModel):
#     name: str = Field(
#         title="category name",
#         description="The name of the AI Product",
#         max_length=50,
#         min_length=3

#     ),
#     price: float = Field(
#         gt=0,
#         title="product price",
#         description="The price is USD, must be greater than zero"
#     )
#     category: Category | None = Field(
#         default=None,
#         title="product category",
#         description="The category to which the product belongs"
#     )

#using field level examples
class Product(BaseModel):
    name:str = Field(examples=["ai"])
    price:float= Field(examples=[23.46])

#using pydentics json_schema_extractor level examples

mode_config = {
    "json_schema_extractor":{
        "examples":[
            {
                "name":"ai"
            }
        ]
    }
}


@app.post("/product")
async def create_product(product:Product):
    return product