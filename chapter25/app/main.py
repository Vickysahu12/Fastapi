from services.services import *
import asyncio

async def main():
    # Create tables
    #await create_tables()
    
    # Create User
    await create_user("Sweety", "sweety@example.com")
    #await create_user("vicky","vicky@example.com")

    #print(await get_all_user())

asyncio.run(main())