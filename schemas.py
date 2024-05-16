from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str

class Recipes(BaseModel):
    id: int
    name: str
    ingredients: str
    instructions: str
    user_id: int

    class Config:
        orm_mode = True
