from fastapi import FastAPI

app = FastAPI()

# @app.get("/student/{student_id}")
# async def student_details(student_id:int):
#     return{"response":"vickys student id is {student_id}", "student_id":student_id}


# in backend always orders matters because when we gave 2parameters one is static and other is dynamic if we
# write dynamic first then write the static code then the static one is not working here is the example:
# so for this when we have static path parameters that should be in above the dynamic one :

@app.get("/student/hello-baccho")
async def student_details_static():
    return{"response":"single data fetched"}

@app.get("/student/{student_name}")
async def student_details(student_name:str):
    return{"response":"vickys student id is {student_name}", "student_name":student_name}

# @app.get("/student/hello-baccho")
# async def student_details_static():
#     return{"response":"single data fetched"}