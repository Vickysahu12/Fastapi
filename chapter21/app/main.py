from database.db import Base, engine, SessionLocal
from models.models import User, Profile, Post, Tag

# Tables create karo
Base.metadata.create_all(bind=engine)

# Session open
db = SessionLocal()

# 🧑 Create User
user1 = User(name="Vicky", email="vicky@example.com")

# 🪪 One-to-One: Profile
profile1 = Profile(bio="I love coding!", user=user1)

# 📝 One-to-Many: Posts
post1 = Post(title="My First Post", content="Hello world!", user=user1)
post2 = Post(title="SQLAlchemy Rocks", content="Learning relationships!", user=user1)

# 🏷️ Many-to-Many: Tags
tag1 = Tag(name="Python")
tag2 = Tag(name="FastAPI")

post1.tags.extend([tag1, tag2])
post2.tags.append(tag1)

# Add to DB
db.add(user1)
db.commit()

# Query data
users = db.query(User).all()
for u in users:
    print(u, u.profile, u.posts)
