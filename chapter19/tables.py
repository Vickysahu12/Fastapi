from db import engine
from sqlalchemy import MetaData,Table,Column,Integer,String,ForeignKey

metadata = MetaData()

# How to make a table :
users = Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(length=50)),
    Column("email",String, nullable=False, unique=True)
)

# lets make an another table
# one to many reelational table
posts = Table(
    "posts",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("user_id",Integer,ForeignKey("users.id",ondelete="CASCADE"), nullable=False),
    Column("Title",String,nullable=False),
    Column("Content",String,nullable=False)
)


#create table in database
def create_tables():
    metadata.create_all(engine)