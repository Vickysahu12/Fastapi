from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()
# Learn about Dependecies with yield

# class OwnerError(Exception):
#     pass

# def get_username():
#     try:
#         yield "Alok"
#     except OwnerError as e:
#         raise HTTPException(status_code=400, detail=f"owner error:{e}")

# @app.get("/item/{item_id}")
# def get_items(item_id:str, username: Annotated[str, Depends(get_username)]):
#     data = {
#         "LRDI":
#         {"description":"Essential for cracking CAT",
#          "owner":"vicky"},
#          "QUANT":
#          {"description":"Essential for getting IIT BOMBAY",
#          "owner":"Alok"},
#     }

#     if item_id not in data:
#         raise HTTPException(status_code=404, detail="Item Not Found")
    
#     item = data[item_id]

#     if item["owner"] != username :
#         raise OwnerError(username)
    
#     return item

class UserError(Exception):
    pass

def get_username():
    try:
        yield "sweety"
    except UserError as u:
        raise HTTPException(status_code=404,detail=f"owner error:{u}")