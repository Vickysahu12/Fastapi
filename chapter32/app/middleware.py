# from fastapi import Request

# async def users_only(request:Request, call_next):
#     if request.url.path.startswith("/users"):
#         print("Middleware: Before Processing The Request")
#         response = await call_next(request)
#         print("1st Middleware: After Processing The Request, Before Returning Response")
#         return response
#     else:
#         print(f"Middleware:Skipping Middleware for this path {request.url.path}")
#         response = await call_next(request)
#         return response
    
# async def Products_only(request:Request, call_next):
#     if request.url.path.startswith("/Product"):
#         print("Middleware: Before Processing The Request")
#         response = await call_next(request)
#         print(" Middleware: After Processing The Request, Before Returning Response")
#         return response
#     else:
#         print(f"Middleware:Skipping Middleware for this path {request.url.path}")
#         response = await call_next(request)
#         return response
    
# Built-in Middleware (ASGI)
class CustomLoggingMiddleware:
    def __init__(self,app, prefix="LOG"):
        self.app = app
        self.prefix = prefix

    async def __call__(self, scope, receive, send):
        print(f"{self.prefix}: Before Processing request(scope:{scope ['type']})")
        await self.app(scope, receive, send)
        print(f"{self.prefix}: After processing request")