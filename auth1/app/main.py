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
async def main():
     return{
        "me":"Hey Guys I am vickyyy",
        "dream":"I want to make my own edtech startup "
    }


@app.get("/dream")
async def main():
     return{
        "dream1":"Crack the CAT with 99.37 percentile in 2026",
        "dream2":"Launch my edtech startup and grow it to atleast as a revenue 5lakh a month before the year 2026 "
    }

