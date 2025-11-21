from fastapi import FastAPI,Header,Depends,HTTPException
from typing import Annotated
from app.routers import router

app = FastAPI()

# Dependencies in path Operation Decorators:
# async def verify_token(x_token:Annotated[str,Header()]):
#     if x_token != "CAT_99.29":
#         raise HTTPException(status_code=404, detail="X-token header is invalid")
    
# @app.get("/items", dependencies=[Depends(verify_token)])
# async def read_items():
#     return {"data":"Vicky Cracks The IIT BOMBAY WITH HIS EDTECH STARTUP AND ZIPPIT WITH 99.29 percentile"}

# Dependecies for a group path Operation:
app.include_router(router)
