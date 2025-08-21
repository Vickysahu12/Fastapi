from fastapi import FastAPI,Path
from typing import Annotated

app = FastAPI()

products = [
    {"id": 1, "title": "Pencil", "price": 5, "description": "A smooth writing wooden pencil."},
    {"id": 2, "title": "Notebook", "price": 50, "description": "200-page ruled notebook for daily use."},
    {"id": 3, "title": "Eraser", "price": 3, "description": "Soft eraser for clean erasing without tearing paper."},
    {"id": 4, "title": "Geometry Box", "price": 120, "description": "Complete geometry set with compass, scale, protractor."},
    {"id": 5, "title": "Color Crayons", "price": 60, "description": "12 vibrant color crayons for kids."}
]

#numeric validation

@app.get("/products/{product_id}")
async def get_product(product_id:Annotated[int,Path(ge=1,le=6)]):
    for product in products:
        if product["id"] == product_id:
            return product
    return{"error":"product not found"}