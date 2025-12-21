from fastapi import FastAPI 
from contextlib import asynccontextmanager
from app.db.config import create_tables
# from app.account.models import User,RefreshToken
from app.account.routers import router as account_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(account_router)

@app.get("/me")
async def main():
     return{
        "me":"Hey Guys I am vickyyy",
        "dream":"I want to be an entreprenuer"
    }

@app.get("/vicky")
async def mine():
     return{
          "data":"lets start the journey again"
     }

@app.get("/restart")
async def restart():
     return{
          "me":"Hyyy vicky restart again and do the fucking task"
     }