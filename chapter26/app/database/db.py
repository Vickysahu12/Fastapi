from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker

DATBASE_URL = "sqlite+aiosqlite:///Sneha.db"

engine = create_async_engine(DATBASE_URL,echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)