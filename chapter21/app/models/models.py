from sqlalchemy import String, ForeignKey, Table, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db import Base

# 🔗 Many-to-Many Table (Post <-> Tag)
post_tag_table = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)

# 👤 User Model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    # One-to-One: User -> Profile
    profile: Mapped["Profile"] = relationship("Profile", back_populates="user", uselist=False, cascade="all, delete")

    # One-to-Many: User -> Post
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

# 🪪 Profile Model
class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[str] = mapped_column(String(200), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"<Profile(id={self.id}, bio={self.bio})>"

# 📝 Post Model
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship("User", back_populates="posts")

    # Many-to-Many: Post -> Tags
    tags: Mapped[list["Tag"]] = relationship("Tag", secondary=post_tag_table, back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title})>"

# 🏷️ Tag Model
class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)

    posts: Mapped[list["Post"]] = relationship("Post", secondary=post_tag_table, back_populates="tags")

    def __repr__(self):
        return f"<Tag(id={self.id}, name={self.name})>"
