from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

class Recipes(BaseModel):
    id: int
    name: str
    ingredients: str

class Category(BaseModel):
    id: int
    category: str

class Tag(BaseModel):
    id: int
    tag: str

    class Config:
        orm_mode = True
