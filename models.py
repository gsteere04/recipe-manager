from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    # Relationship with Recipe
    recipes = relationship("Recipe", back_populates="owner", cascade="all, delete-orphan")

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String, index=True)
    instructions = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship with User
    owner = relationship("User", back_populates="recipes")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Relationships
    user = relationship("User", back_populates="comments")
    recipe = relationship("Recipe", back_populates="comments")

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Relationships
    user = relationship("User", back_populates="likes")
    recipe = relationship("Recipe", back_populates="likes")

# Add back_populates to Recipe for comments and likes relationships
Recipe.comments = relationship("Comment", back_populates="recipe", cascade="all, delete-orphan")
Recipe.likes = relationship("Like", back_populates="recipe", cascade="all, delete-orphan")

# Add back_populates to User for comments and likes relationships
User.comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")
User.likes = relationship("Like", back_populates="user", cascade="all, delete-orphan")
