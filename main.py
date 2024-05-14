from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas, crud
from database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

def get_users(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

def create_recipe(recipe: schemas.Recipes, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db,recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

def get_recipes(db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db)
    return recipes


