from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///bunny.db"

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(bind=engine,expire_on_commit=False)

# Lets from tomoorrow making the most famous news app of this generation FlashFeed,Zippit
