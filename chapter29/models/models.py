from sqlmodel import Field,SQLModel,Relationship


class UserAddressLink(SQLModel,table=True):
    user_id:int = Field(foreign_key="user.id", primary_key=True, ondelete="CASCADE")
    address_id:int = Field(foreign_key="address.id", primary_key=True, ondelete="CASCADE")

class User(SQLModel, table=True):
    id:int = Field(primary_key=True)
    name:str = Field(nullable=False)
    email:str

    profile: "Profile" = Relationship(back_populates="user",cascade_delete=True)
    posts: list["Post"] = Relationship(back_populates="user")
    address:list["Address"] = Relationship(back_populates="user", link_model=UserAddressLink)

class Owner(SQLModel, table=True):
    id:int = Field(primary_key=True)
    name:str  = Field(nullable=False)
    email:str = Field(nullable=False)
    
# one-to-one
class Profile(SQLModel,table=True):
    id:int = Field(primary_key=True)
    user_id:int = Field(foreign_key="user.id", unique=True, ondelete="CASCADE")
    bio:str

    user: "User" = Relationship(back_populates="profile")

# one-to-many
class Post(SQLModel,table=True):
    id:int = Field(primary_key=True)
    user_id:int = Field(foreign_key="user.id", ondelete="SET NULL", nullable=True)
    title:str
    content:str

    user: "User" = Relationship(back_populates="posts")

# Many-to-Many
class Address(SQLModel,table=True):
    id:int = Field(primary_key=True)
    street:str
    city:str

    user:"User" = Relationship(back_populates="address", link_model=UserAddressLink)