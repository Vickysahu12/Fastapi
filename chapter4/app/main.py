from fastapi import FastAPI
from enum import Enum

app = FastAPI()

## how to give predefined values 
## here we define a enum class with allowed product categories
class SubjectCategory(str, Enum):
    science = "science"
    math = "math"
    english = "english"
    manner = "manner"

## here we use the enum as the type for the parameter
# @app.get("/video/{category}")
# async def get_video(category: SubjectCategory):
#     return{"response":"videos are fetched", "category":category}

# working with python enumaration :
@app.get("/video/{category}")
async def get_video(category: SubjectCategory):
    if category == SubjectCategory.english:
        return{"category":category,"message":"The story of english is awesome and the practice question are also awesome"}
    elif category.value == "math":
        return{"message":"math story and questions are awesome"}
    elif category.value == "manner":
        return{"message":"the story of manner is just top notch"}
    elif category.value == "science":
        return{"message":"the experiment in science is awesome"}
    else:
        return{"message":"category is unknown"}
    
# path convertor:
@app.get("/files/{file_path:path}")
async def read_path(file_path:str):
    return{"your requestes file at path": file_path}