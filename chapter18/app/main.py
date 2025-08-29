from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse,PlainTextResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

fruits = {
    "apple":"A juicy fruit",
    "banana":"A yellow delight"
}
# using HTTPException
@app.get("/items/{item_id}")
async def item(item_id:str):
    if item_id not in fruits:
        # In this way we can handle exeception handling
        raise HTTPException(status_code=404, detail="items Not found")
    return fruits[item_id]

# Adding Custom Header
@app.get("/items/{item_id}")
async def item(item_id:str):
    if item_id not in fruits:
        # In this way we can handle exeception handling
        raise HTTPException(status_code=404,
                            detail="items Not found",
                            headers={"X-error-type":"ItemsMissing"}
                            )
    return fruits[item_id]

#How To Implement Custom Exception:-
#1. Create Exception
class FruitException(Exception):
    def __init__(self, fruit_name:str):
        self.fruit_name = fruit_name

# 2. Custom Handle Exception:-
@app.exception_handler(FruitException)
async def fruit_exception_handler(request:Request,exc:FruitException):
    return JSONResponse(
        status_code=418,
        content={"message":f"{exc.fruit_name} is not a valid fruit name"}
    )

# 3. Now we will gonna make the route to see how it works
@app.get("/fruits/{fruit_name}")
async def read_fruit(fruit_name:str):
    if fruit_name not in fruits:
        raise FruitException(fruit_name=fruit_name)
    return fruits[fruit_name]

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,exc:RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)

# Override default exception handler :-
@app.get("/items/{item_id}")
async def read_items(item_id:int):
    return item_id