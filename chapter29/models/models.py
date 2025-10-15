from sqlmodel import Field,SQLModel

class User(SQLModel, table=True):
    id:int = Field(primary_key=True)
    name:str = Field(nullable=False)
    email:str

class Owner(SQLModel, table=True):
    id:int = Field(primary_key=True)
    name:str  = Field(nullable=False)
    email:str = Field(nullable=False)
    