from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas, crud
from database import SessionLocal, engine

app = FastAPI()

# Returns database
@app.get("/db")
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User functions, create, and list users
@app.post("/users")
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Returns a sinlge user using user id
@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Returns multiple users
@app.get("/users", response_model=list[schemas.User])
async def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.put("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, user_update: schemas.User, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db=db, user_id=user_id, user_update=user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
# Deletes user using user id
@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Recipe functions, create, list, and delete users.
# Creates a new recipe
@app.post("/recipes")
async def create_recipe(recipe: schemas.Recipes, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

# Returns one recipe using recipe id
@app.get("/recipes/{recipe_id}")
async def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db,recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

# Returns multiple recipes 
@app.get("/recipes", response_model=list[schemas.Recipes])
async def get_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    return recipes

# Updates a specific 
@app.put("/recipes/{recipe_id}", response_model=schemas.Recipes)
async def update_recipe(recipe_id: int, recipe: schemas.Recipes, db: Session = Depends(get_db)):
    updated_recipe = crud.update_recipe(db=db, recipe_id=recipe_id, recipe=recipe)
    if updated_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return updated_recipe


