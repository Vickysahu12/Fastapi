from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./smruti.db"

engine = create_async_engine(DATABASE_URL,echo=True)
