from fastapi import FastAPI,Cookie,Body,Header
from typing import Annotated
from pydantic import BaseModel, Field
app = FastAPI()

#for checking cookie parameter 
# curl -H "Cookie: session_id=abc123" http://127.0.0.1:8000/students/recommendations
# {"message":"students details for sessionabc123","session_id":"abc123"}

# Now we will gonna learn cookie parameter
# @app.get("/students/recommendations")
# async def get_recommendations(session_id:Annotated[str | None,Cookie()] = None):
#     if session_id:
#         return{"message":f"students details for session{session_id}","session_id":session_id}
#     return{"message":"No session id provide showing default recommenadations"}

# cookie with pydantic model
class ProductCookies(BaseModel):
    session_id:str
    prefered_category:str | None = None
    tracking_id:str | None = None

@app.get("/students/recommendations")
async def get_recommend(cookies:Annotated[ProductCookies,Cookie()]):
    response = {"session_id":cookies.session_id}
    if cookies.prefered_category:
        response["message"] = f"Recommendation for {cookies.prefered_category} Products"
    else:
        response["message"] = f"Default recommendation for session {cookies.session_id}"
    if cookies.tracking_id:
        response["tracking_id"] = cookies.tracking_id
    return response

#header parameters 
@app.get("/students")
async def get_students(user_agent: Annotated[str | None , Header()] = None):
    return user_agent