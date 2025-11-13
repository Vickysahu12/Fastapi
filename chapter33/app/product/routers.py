from fastapi import APIRouter

router = APIRouter(
    prefix="/product",
    tags=["product"]
)

@router.get("/")
async def get_all_Product():
    return{"response: All Users"}

@router.get("/{product_id}")
async def get_single_product(product_id:int):
    return {"data": f"User with ID {product_id}"}
