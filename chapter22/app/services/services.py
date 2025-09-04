from models.models import User,Post
from database.db import SessionLocal
from sqlalchemy import select

# Insert or Create a User
def create_user(name: str, email:str):
    with SessionLocal() as session:
        user = User(name=name,email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
# Insert or Create post
def create_post(id: int, title:str,content:str,user_id:int):
    with SessionLocal() as session:
        post = Post(id=id,title=title,content=content,user_id=user_id)
        session.add(post)
        session.commit()
        
# Read User By ID
def get_user_by_id(user_id:int):
    with SessionLocal() as session:
        user = session.get_one(User,user_id)
        return user
    
# Read Post By Id
# def get_post_by_id(post_id:int):
#     with SessionLocal() as session:
#         post = session.get_one(Post,post_id)
#         return post
    
# Different method to Read Post By Id
def get_post_by_id(post_id:int):
    with SessionLocal() as session:
        stmt = select(Post).where(Post.id == post_id)
        post = session.scalars(stmt).one()
        return post


# Read All User
def get_all_user():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()
        return users
    
# Read-post By User :
def get_posts_by_user(user_id:int):
    with SessionLocal() as session:
        user = session.get(User,user_id)
        posts = user.posts if user else []
        return posts


# Update User Email:
def update_user_email(user_id:int,new_email:str):
    with SessionLocal() as session:
        user = session.get(User,user_id)
        if user:
            user.email = new_email
            session.commit()
        return user
    
# Delete Posts :-
def delete_post(post_id:int):
    with SessionLocal() as session:
        post = session.get(Post,post_id)
        if post:
            session.delete(post)
            session.commit()

# sry for todays i have some issues thats why i cant able to do the todays session 