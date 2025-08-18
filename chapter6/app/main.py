from fastapi import FastAPI

app = FastAPI()

# single query Parameter
@app.get("/products")
async def main(category:str):
    return{
        "status":"okk",
        "category":category
    }

# multiple query Parameter
@app.get("/products")
async def main(category:str,limit:int):
    return{
        "status":"okk",
        "category":category,
        "limit":limit
    }

#deafult quesry parameter
@app.get("/products")
async def main(category:str,limit:int=20):
    return{
        "status":"okk",
        "category":category,
        "limit":limit
    }


#default quesry parameter
@app.get("/products")
async def main(limit:int=20,category:str=None):
    return{
        "status":"okk",
        "category":category,
        "limit":limit
    }