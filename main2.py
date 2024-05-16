from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas, crud
from database import SessionLocal, engine

app = FastAPI()

@app.get("/db")
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creates a new user
@app.post("/users")
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

#Gets a specific user by their ID
@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Returns a list of al users
@app.get("/users", response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.patch("/users/{user_id}")
async def change_user_name(user_id: int, db: Session = Depends(get_db)):
    try:
        updated_name = crud.updated_user(db, user_id)
        if not updated_name:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User updated successfully"}
    finally:
        db.close()

#Deletes selected user by ID
@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        deleted = crud.delete_user(db,user_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
    finally:
        db.close()


@app.post("/recipes")
async def create_recipe(recipe: schemas.Recipes, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db,recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.get("/recipies",response_model=list[schemas.Recipes])
async def get_recipes(db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db) 
    return recipes

@app.patch("/recipes/{recipe_id}")
async def update_recipe(recipe_id: int, updated_recipe: schemas.Recipes, db: Session = Depends(get_db)):
    try:
        updated = crud.update_recipe(db, recipe_id, updated_recipe)
        if not updated:
            raise HTTPException(status_code=404, detail="Recipe not found")
        return {"message": "Recipe updated successfully"}
    finally:
        db.close()

@app.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    try:
        deleted = crud.delete_recipe(db,recipe_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Recipe not found")
        return {"message": "Recipe deleted successfully"}
    finally:
        db.close()


