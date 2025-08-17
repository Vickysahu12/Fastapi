from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":'Lets start the amazing journey of fastapi'}