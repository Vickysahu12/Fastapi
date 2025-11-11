from fastapi import Request

async def my_first_middleware(request:Request, call_next):
    print("1st Middleware:Before Processing the Request")
    response = await call_next(request)
    print("1st Middleware:After Processing the Request, After returning response")
    return response

async def my_second_middleware(request:Request, call_next):
    print("2nd Middleware:Before Processing the Request")
    response = await call_next(request)
    print("2nd Middleware:After Processing the Request, After returning response")
    return response