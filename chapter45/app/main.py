from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables from .env files
load_dotenv()

app = FastAPI()

@app.get("/")
def read_env():
    return{
        "api-secret": os.getenv("API_SECRET_KEY"),
        "debug_mode": os.getenv("DEBUG")
    }

@app.get("/me")
def read_env():
    return{
        "api-secret": os.getenv("API_SECRET_KEY"),
        "debug_mode": os.getenv("DEBUG")
    }

