from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/items")
async def all_items():
    return "all items"

@app.get("/me")
async def me():
    return "hey this is me 'vicky'"