from fastapi import FastAPI,Query
from typing import Annotated

app = FastAPI()

products = [
    {"id": 1, "title": "Pencil", "price": 5, "description": "A smooth writing wooden pencil."},
    {"id": 2, "title": "Notebook", "price": 50, "description": "200-page ruled notebook for daily use."},
    {"id": 3, "title": "Eraser", "price": 3, "description": "Soft eraser for clean erasing without tearing paper."},
    {"id": 4, "title": "Geometry Box", "price": 120, "description": "Complete geometry set with compass, scale, protractor."},
    {"id": 5, "title": "Color Crayons", "price": 60, "description": "12 vibrant color crayons for kids."}
]

# basic query parameter:
# @app.get("/products")
# async def all_prod(search: str | None = None):
#     if search:
#         search_lower = search.lower()
#         filter_product = []
#         for product in products:
#             if search_lower in product['title'].lower():
#                 filter_product.append(product)
#         return filter_product   # <-- loop ke baad return
#     return products



# #validation with annotated
# @app.get("/products")
# async def all_prod(search: str | None = Query(default=None,max_length=7)):
#     if search:
#         search_lower = search.lower()
#         filter_product = []
#         for product in products:
#             if search_lower in product['title'].lower():
#                 filter_product.append(product)
#         return filter_product   # <-- loop ke baad return
#     return products


#validation with annotated
# @app.get("/products")
# async def all_prod(
#     search: 
#     Annotated[
#         str | None, 
#         Query(max_length=7)] 
#         = None):
#     if search:
#         search_lower = search.lower()
#         filter_product = []
#         for product in products:
#             if search_lower in product['title'].lower():
#                 filter_product.append(product)
#         return filter_product   # <-- loop ke baad return
#     return products

## Multiple search terms (List)
@app.get("/products")
async def get_products(search:Annotated[list[str] | None, Query()] = None):
    if search:
        filter_product = []
        for product in products:
            for s in search:
                if s.lower() in product["title"].lower():
                    filter_product.append(product)
        return filter_product
    return product