from fastapi import FastAPI,Body,Cookie,Header
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class StudentData(BaseModel):
    name:str
    age:int
    course:str

class CookieSession(BaseModel):
    session_id:str
    prefered_category:str | None = None
    tracking_id:str | None = None

@app.post("/students/details")
async def student_details(student:Annotated[StudentData,Body()],
                          cookies: Annotated[CookieSession,Cookie()] = None,
                          user_agent:Annotated[str | None , Header()]=None
                          ):
    response = {
        "student":student.dict(),
        "cookies":cookies.dict() if cookies else "No Cokkies found",
        "user_agent":user_agent
    }
    return response

# By using this we will gonna get our answer from our cmd terminal
# curl -X POST "http://127.0.0.1:8000/students/details" -H "Content-Type: application/json" -H "User-Agent: CustomBrowser/1.0" -H "Cookie: session_id=abc123; prefered_category=Math; tracking_id=vicky786" -d "{\"name\":\"Vicky\",\"age\":21,\"course\":\"BCA\"}"
