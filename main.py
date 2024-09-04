from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas, crud
from database import SessionLocal, engine

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User CRUD Operations

@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users", response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.patch("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, updated_name: str, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, updated_name)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

# Recipe CRUD Operations

@app.post("/recipes", response_model=schemas.Recipe)
async def create_recipe(recipe: schemas.Recipe, db: Session = Depends(get_db)):
    return crud.create_recipe(db=db, recipe=recipe)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
async def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.get("/recipes", response_model=list[schemas.Recipe])
async def get_recipes(db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db)
    return recipes

@app.patch("/recipes/{recipe_id}", response_model=schemas.Recipe)
async def update_recipe(recipe_id: int, updated_recipe: schemas.Recipe, db: Session = Depends(get_db)):
    recipe = crud.update_recipe(db, recipe_id, updated_recipe)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.delete("/recipes/{recipe_id}", response_model=dict)
async def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_recipe(db, recipe_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted successfully"}

# Comment CRUD Operations

@app.post("/comments", response_model=schemas.Comment)
async def create_comment(comment: schemas.Comment, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

@app.get("/comments/{comment_id}", response_model=schemas.Comment)
async def get_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = crud.get_comment(db, comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@app.get("/comments", response_model=list[schemas.Comment])
async def get_comments(db: Session = Depends(get_db)):
    comments = crud.get_comments(db)
    return comments

@app.patch("/comments/{comment_id}", response_model=schemas.Comment)
async def update_comment(comment_id: int, updated_comment: schemas.Comment, db: Session = Depends(get_db)):
    comment = crud.update_comment(db, comment_id, updated_comment)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@app.delete("/comments/{comment_id}", response_model=dict)
async def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_comment(db, comment_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted successfully"}

# Like CRUD Operations

@app.post("/likes", response_model=schemas.Like)
async def create_like(like: schemas.Like, db: Session = Depends(get_db)):
    return crud.create_like(db=db, like=like)

@app.get("/likes/{like_id}", response_model=schemas.Like)
async def get_like(like_id: int, db: Session = Depends(get_db)):
    like = crud.get_like(db, like_id)
    if like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return like

@app.get("/likes", response_model=list[schemas.Like])
async def get_likes(db: Session = Depends(get_db)):
    likes = crud.get_likes(db)
    return likes

@app.delete("/likes/{like_id}", response_model=dict)
async def delete_like(like_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_like(db, like_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Like not found")
    return {"message": "Like deleted successfully"}
