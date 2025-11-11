# How to Create a Middleware in FASTApi
from fastapi import FastAPI
from middlewares import my_first_middleware,my_second_middleware

app = FastAPI()

# Creating Middleware:
app.middleware('http')(my_first_middleware)
app.middleware('http')(my_second_middleware)

# The Middleware execute from Bottom to top :


@app.get("/user")
async def get_users():
    print("Endpoint:Inside get_users endpoint")
    return {"data":"All Users Data"}

@app.get("/Product")
async def get_Product():
    print("Endpoint:Inside get_Product endpoint")
    return {"data":"All Product Data"}