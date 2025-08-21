from fastapi import FastAPI,status

app = FastAPI()

products = [
    {
        "id": 1,
        "title": "Pencil",
        "price": 5,
        "description": "A smooth writing wooden pencil."
    },
    {
        "id": 2,
        "title": "Notebook",
        "price": 50,
        "description": "200-page ruled notebook for daily use."
    },
    {
        "id": 3,
        "title": "Eraser",
        "price": 3,
        "description": "Soft eraser for clean erasing without tearing paper."
    },
    {
        "id": 4,
        "title": "Geometry Box",
        "price": 120,
        "description": "Complete geometry set with compass, scale, protractor."
    },
    {
        "id": 5,
        "title": "Color Crayons",
        "price": 60,
        "description": "12 vibrant color crayons for kids."
    }
]

@app.get("/")
async def main_route():
    return {"write /product to go to the product_list route page"}

#all product fetching
@app.get("/product",status_code=status.HTTP_200_OK)
async def prod_list():
    return products

# single product fetching
@app.get("/product/{product_id}")
async def sing_prod(product_id:int):
    for product in products:
        if product['id'] == product_id:
            return product
        
# post request
## create or insert data
@app.post("/product",status_code=status.HTTP_201_CREATED)
async def create_prod(new_product:dict):
    products.append(new_product)
    return{"response":"created","new_product":new_product}

# put request
##update complete data
@app.put("/product/{product_id}")
async def prop_update(product_id:int, new_updated_product:dict):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            product[index] = new_updated_product
            return{
                "status":"product updated", 
                "product_id":product_id, 
                "new_updated_product":new_updated_product
            }
        
@app.patch("/product/{product_id}")
async def partial_prod_update(product_id:int,new_updated_product:dict):
    for product in products:
        if product["id"] == product_id:
            product.update(new_updated_product)
            return{
                "status":"partial updated",
                "product_id":product_id,
                "new_updated_product":new_updated_product
            }
        
@app.delete("/product/{product_id}")
async def product_delete(product_id:int):
    for index,product in enumerate(products):
        if product["id"] == product_id:
            products.pop(index)
            return{"status":"product deleted", "product_id":product_id}
        
