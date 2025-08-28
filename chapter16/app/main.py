from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

@app.get("/",response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2>Login Form</h2>
            <form action="/login/" method="post">
                <label for="Username">Username:</label><br>
                <input type="text" id="username"
                name="username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
"""

# @app.post("/login/")
# async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
#     return{"username":username,"password":password}



# Now we will gonna use pydantic to make it more modular and clean
class FormData(BaseModel):
    username:str
    password:str

@app.post("/login/")
async def login(data:Annotated[FormData,Form()]):
    return data