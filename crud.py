from sqlalchemy.orm import Session
import models

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

def updated_user(db: Session, user_id: int, updated_name: str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.username = updated_name
        db.commit()
        db.refresh(user)
        return user
    
def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

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
        recipe.id = updated_recipe.id
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

#def create_category(db: Session, category: models.Category):
#    db_category = models.Category(**models.Category.model_dump())
#    db.add(db_category)
#    db.commit()
#    db.refresh(db_category)
#    return db_category


