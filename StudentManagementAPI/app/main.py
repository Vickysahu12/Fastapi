from fastapi import FastAPI, Header, Cookie
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Student model (body)
class Student(BaseModel):
    name: str
    age: int
    course: str

# ✅ 1. Add Student API (POST)
@app.post("/students/add")
async def add_student(
    student: Student,
    user_agent: Optional[str] = Header(None),
    session_id: Optional[str] = Cookie(None)
):
    return {
        "message": f"Student {student.name} added successfully!",
        "student_data": student.dict(),
        "headers": {
            "User-Agent": user_agent
        },
        "cookies": {
            "session_id": session_id
        }
    }

# ✅ 2. Get Student Details API (GET with query param)
@app.get("/students/details")
async def get_student(
    name: str,
    tracking_id: Optional[str] = Cookie(None)
):
    return {
        "student": {
            "name": name,
            "status": "Active"
        },
        "cookies": {
            "tracking_id": tracking_id
        }
    }

# ✅ 3. Update Student Course (PUT)
@app.put("/students/update")
async def update_course(
    student: Student,
    prefered_category: Optional[str] = Cookie(None)
):
    return {
        "message": f"Course updated for {student.name}",
        "updated_data": student.dict(),
        "cookies": {
            "prefered_category": prefered_category
        }
    }

# for post we will gonna use in cmd this line :
# curl -X POST "http://127.0.0.1:8000/students/add" -H "Content-Type: application/json" -H "User-Agent: CustomBrowser/1.0" -H "Cookie: session_id=abc123" -d "{\"name\":\"Vicky\",\"age\":21,\"course\":\"BCA\"}"

# for put we will gonna use this
# curl -X PUT "http://127.0.0.1:8000/students/update" -H "Content-Type: application/json" -H "Cookie: prefered_category=Math" -d "{\"name\":\"Vicky\",\"age\":21,\"course\":\"AI\"}"

# for get we will gonna use this 
# curl -X GET "http://127.0.0.1:8000/students/get/Vicky" -H "User-Agent: CustomBrowser/1.0" -H "Cookie: session_id=abc123"

 