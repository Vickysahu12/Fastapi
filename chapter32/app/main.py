from fastapi import FastAPI
from middleware import CustomLoggingMiddleware
#from middleware import users_only, Products_only

app = FastAPI()

app.add_middleware(CustomLoggingMiddleware, prefix="CUSTOM_LOG")

# app.middleware("http")(users_only)
# app.middleware("http")(Products_only)

@app.get("/users")
async def all_user():
    print("Endpoint: Fetch All The User")
    return{"data: All Users Data"}

@app.get("/Product")
async def all_user():
    print("Endpoint: Fetch All The Product")
    return{"data: All Product Data"}

# We can made Built in middleware according to our usage 
# ASGI middlewares are custom or third party middlewares that follows the ASGI spec.
# ASGI middlewares are typically classes that take an ASGI app and configuration Parameters.