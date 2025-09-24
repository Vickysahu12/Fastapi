from models.models import create_tables,drop_tables
from services.services import *
import asyncio

async def main():
    # Create Tables
    #await create_tables()
    #await create_user("vicky", "vicky@example.com")
    await create_user("chutki", "chutki@example.com")

asyncio.run(main())