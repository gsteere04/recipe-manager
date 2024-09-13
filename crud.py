from sqlalchemy.orm import Session
import models, schemas  # Add this import

# User CRUD Operations
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, updated_name: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.username = updated_name
        db.commit()
        db.refresh(user)
        return user
    return None

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        # Delete related likes
        db.query(models.Like).filter(models.Like.user_id == user_id).delete()
        # Delete related comments
        db.query(models.Comment).filter(models.Comment.user_id == user_id).delete()
        # Delete related recipes
        db.query(models.Recipe).filter(models.Recipe.user_id == user_id).delete()
        # Delete the user
        db.delete(user)
        db.commit()
        return True
    return False

# Recipe CRUD Operations
def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def update_recipe(db: Session, recipe_id: int, recipe_update: schemas.RecipeUpdate):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if db_recipe:
        update_data = recipe_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_recipe, key, value)
        db.commit()
        db.refresh(db_recipe)
    return db_recipe

def delete_recipe(db: Session, recipe_id: int):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if recipe:
        db.delete(recipe)
        db.commit()
        return True
    return False

# Comment CRUD Operations
def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).offset(skip).limit(limit).all()

def update_comment(db: Session, comment_id: int, comment_update: schemas.CommentUpdate):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment:
        update_data = comment_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_comment, key, value)
        db.commit()
        db.refresh(db_comment)
        return db_comment
    return None

def delete_comment(db: Session, comment_id: int):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
        return True
    return False

# Like CRUD Operations
def create_like(db: Session, like: schemas.LikeCreate):
    db_like = models.Like(**like.model_dump())
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def get_like(db: Session, like_id: int):
    return db.query(models.Like).filter(models.Like.id == like_id).first()

def get_likes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Like).offset(skip).limit(limit).all()

def delete_like(db: Session, like_id: int):
    like = db.query(models.Like).filter(models.Like.id == like_id).first()
    if like:
        db.delete(like)
        db.commit()
        return True
    return False

def update_like(db: Session, like_id: int, like_update: dict):
    db_like = db.query(models.Like).filter(models.Like.id == like_id).first()
    if db_like:
        for key, value in like_update.items():
            setattr(db_like, key, value)
        db.commit()
        db.refresh(db_like)
        return db_like
    return None

# New methods to get user's comments and liked recipes
def get_user_comments(db: Session, user_id: int):
    return db.query(models.Comment).filter(models.Comment.user_id == user_id).all()

def get_user_liked_recipes(db: Session, user_id: int):
    likes = db.query(models.Like).filter(models.Like.user_id == user_id).all()
    return [like.recipe for like in likes]
