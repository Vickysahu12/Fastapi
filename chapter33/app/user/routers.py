from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/")
async def get_all_users():
    return{"response: All Users"}

@router.get("/{user_id}")
async def get_single_user(user_id:int):
    return {"data": f"User with ID {user_id}"}
