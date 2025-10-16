from sqlmodel import Session,select
from db.db import engine
from models.models import User,Owner

def create_user(name:str,email:str):
    with Session(engine) as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    

def create_owner(name:str,email:str):
    with Session(engine) as session:
        owner = Owner(name=name, email=email)
        session.add(owner)
        session.commit()
        session.refresh(owner)
        return owner
    
def get_all_users():
    with Session(engine) as session:
        stmt = select(User)
        users = session.exec(stmt)
        return users.all()
    
def get_user(user_id:int):
    with Session(engine) as session:
        stmt = select(User).where(User.id == user_id)
        user = session.exec(stmt).first()
        return user