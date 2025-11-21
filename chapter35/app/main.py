from fastapi import FastAPI,Depends
from typing import Annotated

app=FastAPI()

#sync-dependecy
# def sync_dep():
#     return{"message":"I am sync"}

# #Async dependency
# async def async_dep():
#     return{"message":"I am async"}

# @app.get("/test/")
# async def test(
#     sync:Annotated[dict,Depends(sync_dep)],
#     Async:Annotated[dict,Depends(async_dep)],
# ):
#     return{"sync":sync,"async":A}

# Hierarchical Dependecies:
# async def user_auth():
#     return {"user_id":"123"}

# async def user_role(user: Annotated[dict,Depends(user_auth)]):
#     return {"user_id":user["user_id"], "role":"admin"}

# @app.get("/admin")
# async def admin_only(role:Annotated[dict,Depends(user_role)]):
#     return role

# Create Dependency Class
class CommonQueryParams:
    def __init__(self, q:str | None = None, skip: int=0, limit:int=100):
        self.q = q
        self.skip = skip
        self.limit = limit


# Using Dependency endpoint:
@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    return commons