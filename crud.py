from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.User):
    db_user = schemas.User(**schemas.User.model_dump())
    db.add(db_user)
    db.commit
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(schemas.User).filter(schemas.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(schemas.User).offset(skip).limit(limit).all()

def create_recipe(db: Session, recipe: schemas.Recipes):
    db_recipe = schemas.Recipes(**schemas.Recipes.model_dump())
    db.add(db_recipe)
    db.commit
    db.refresh(db_recipe)
    return db_recipe

def get_recipe(db: Session, recipe_id: int):
    return db.query(schemas.Recipes).filter(schemas.Recipes.id == recipe_id).first()

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(schemas.Recipes).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.Category):
    db_category = schemas.Category(**schemas.Category.model_dump())
    db.add(db_category)
    db.commit
    db.refresh(db_category)
    return db_category


