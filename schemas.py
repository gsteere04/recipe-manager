from pydantic import BaseModel, ConfigDict
from typing import Optional, ForwardRef, List

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

# Forward references
CommentRef = ForwardRef('Comment')
LikeRef = ForwardRef('Like')

class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class RecipeBase(BaseModel):
    title: str
    description: str
    ingredients: str
    instructions: str

class RecipeCreate(RecipeBase):
    user_id: int

class RecipeUpdate(BaseModel):
    instructions: str | None = None
    ingredients: str | None = None

class Recipe(RecipeBase):
    id: int
    user_id: int
    instructions: str | None = None
    ingredients: str | None = None
    model_config = ConfigDict(from_attributes=True)

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    user_id: int
    recipe_id: int

class CommentUpdate(BaseModel):
    content: str | None = None

class Comment(CommentBase):
    id: int
    user_id: int
    recipe_id: int
    model_config = ConfigDict(from_attributes=True)

class LikeBase(BaseModel):
    user_id: int
    recipe_id: int

class LikeCreate(LikeBase):
    pass

class LikeUpdate(BaseModel):
    user_id: int | None = None
    recipe_id: int | None = None

class Like(LikeBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class RecipeUpdate(BaseModel):
    title: str | None = None
    ingredients: str | None = None
    instructions: str | None = None
    user_id: int | None = None
    model_config = ConfigDict(from_attributes=True)

class CommentUpdate(BaseModel):
    content: str | None = None
    model_config = ConfigDict(from_attributes=True)

class LikeUpdate(BaseModel):
    user_id: int | None = None
    recipe_id: int | None = None
    model_config = ConfigDict(from_attributes=True)

# Update forward references
for model in [User, Recipe, Comment, Like]:  # Add all your Pydantic models here
    model.model_rebuild()
