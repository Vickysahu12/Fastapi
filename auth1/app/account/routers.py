from fastapi import APIRouter,Depends
from app.account.services import create_user, authenticate_user
from app.account.models import UserCreate, UserOut
from fastapi.security import OAuth2PasswordRequestForm
from app.db.config import SessionDep

router = APIRouter(prefix="/account", tags=["Account"])

@router.post("/register", response_model=UserOut)
def register(session:SessionDep, user:UserCreate):
    return create_user(session, user)

@router.post("/login")
def login(session:SessionDep, form_data:OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(session)