from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./sweety.db"

engine = create_async_engine(DATABASE_URL,echo=True)
