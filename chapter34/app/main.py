# Learning about Creating and Using dependency injection

from fastapi import FastAPI,Depends
from typing import Annotated

app = FastAPI()

# Creating dependency function:
# async def common_parameter(q:str | None = None, skip:float = 0, limit:int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# # Using dependency in endpoint:
# @app.get("/items")
# async def read_items(commons:Annotated[dict,Depends(common_parameter)]):
#     return commons

# @app.get("/users")
# async def read_users(commons:Annotated[dict,Depends(common_parameter)]):
#     return commons

# # we can create Type Alias to not writing the code again and again
# commonsDep = Annotated[dict, Depends(common_parameter)] 

# @app.get("/Product")
# async def read_product(commons:commonsDep):
#     return commons

# Learn How to Make sync and async dependency

# sync dependency
def sync_dep():
    return{"message":"I am sync"}

# Async dependency
def async_dep():
    return{"message":"I am Async"}

@app.get("/test/")
async def test(
    sync_result:Annotated[dict,Depends(sync_dep)],
    async_result:Annotated[dict,Depends(async_dep)],
):
    return {"sync": sync_result, "async": async_result}