from fastapi import APIRouter
from typing import Annotated

router = APIRouter()

@router.get("/items")
async def Crack_CAT():
    return {"data":"LRDI WITH 98.95 percentile"}

