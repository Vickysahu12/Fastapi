from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db_path = os.path.join(BASE_DIR,"bunny.db")

DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(bind=engine,expire_on_commit=False)

# Lets from tomoorrow making the most famous news app of this generation FlashFeed,Zippit
