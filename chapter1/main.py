from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":'Hello Baccho mein apke liye bana raha hun ek scalable backend . hurray.'}