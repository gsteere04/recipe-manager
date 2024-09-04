from sqlalchemy.orm import Session
import models

# User CRUD Operations
def create_user(db: Session, user: models.User):
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
        db.delete(user)
        db.commit()
        return True
    return False

# Recipe CRUD Operations
def create_recipe(db: Session, recipe: models.Recipe):
    db_recipe = models.Recipe(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Recipe).offset(skip).limit(limit).all()

def update_recipe(db: Session, recipe_id: int, updated_recipe: models.Recipe):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if recipe:
        recipe.name = updated_recipe.name
        recipe.ingredients = updated_recipe.ingredients
        recipe.instructions = updated_recipe.instructions
        db.commit()
        db.refresh(recipe)
        return recipe
    return None

def delete_recipe(db: Session, recipe_id: int):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if recipe:
        db.delete(recipe)
        db.commit()
        return True
    return False

# Comment CRUD Operations
def create_comment(db: Session, comment: models.Comment):
    db_comment = models.Comment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).offset(skip).limit(limit).all()

def update_comment(db: Session, comment_id: int, updated_comment: models.Comment):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if comment:
        comment.content = updated_comment.content
        comment.recipe_id = updated_comment.recipe_id
        comment.user_id = updated_comment.user_id
        db.commit()
        db.refresh(comment)
        return comment
    return None

def delete_comment(db: Session, comment_id: int):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
        return True
    return False

# Like CRUD Operations
def create_like(db: Session, like: models.Like):
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
