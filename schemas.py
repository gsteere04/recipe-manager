from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    recipes: List["Recipe"] = []

    class Config:
        orm_mode = True

class RecipeBase(BaseModel):
    name: str
    ingredients: str
    instructions: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    user_id: int
    owner: User

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    user_id: int
    recipe_id: int
    user: User
    recipe: Recipe

    class Config:
        orm_mode = True

class LikeBase(BaseModel):
    pass

class LikeCreate(LikeBase):
    pass

class Like(LikeBase):
    id: int
    user_id: int
    recipe_id: int
    user: User
    recipe: Recipe

    class Config:
        orm_mode = True
