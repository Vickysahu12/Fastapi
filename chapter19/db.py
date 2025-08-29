from sqlalchemy import create_engine
DATABASE_URL = "sqlite:///./vicky.db"

engine = create_engine(DATABASE_URL, echo=True)