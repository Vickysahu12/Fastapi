from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    name:str
    age:int
    favouritesubject:str | None = None

class StudentOut(BaseModel):
    name:str
    age:int

#response model parameter
@app.get("/students/",response_model=Student)
async def get_student():
    return{"name":"vicky","age":19,"favouritesubject":"Coding"}