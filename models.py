from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


    recipes = relationship("Recipe", back_populates="owner")
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    instructions = Column(String, index=True)
    
    owner = relationship("User", back_populates="recipes")


    

