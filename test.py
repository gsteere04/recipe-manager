import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from database import Base, SessionLocal
from main import app, get_db

# Setup for the test database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/recipe_browser"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Test User CRUD operations
def test_create_user():
    response = client.post("/users", json={"username": "testuser"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser"}

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "testuser"}

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_user():
    response = client.patch("/users/1", json={"updated_name": "updateduser"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "username": "updateduser"}

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}

# Test Recipe CRUD operations
def test_create_recipe():
    response = client.post("/recipes", json={"name": "testrecipe", "ingredients": "ingredients", "instructions": "instructions", "user_id": 1})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "testrecipe", "ingredients": "ingredients", "instructions": "instructions", "user_id": 1}

def test_get_recipe():
    response = client.get("/recipes/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "testrecipe", "ingredients": "ingredients", "instructions": "instructions", "user_id": 1}

def test_get_recipes():
    response = client.get("/recipes")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_recipe():
    response = client.patch("/recipes/1", json={"name": "updatedrecipe", "ingredients": "updatedingredients", "instructions": "updatedinstructions", "user_id": 1})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "updatedrecipe", "ingredients": "updatedingredients", "instructions": "updatedinstructions", "user_id": 1}

def test_delete_recipe():
    response = client.delete("/recipes/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Recipe deleted successfully"}

# Test Comment CRUD operations
def test_create_comment():
    response = client.post("/comments", json={"content": "testcomment", "user_id": 1, "recipe_id": 1})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "content": "testcomment", "user_id": 1, "recipe_id": 1}

def test_get_comment():
    response = client.get("/comments/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "content": "testcomment", "user_id": 1, "recipe_id": 1}

def test_get_comments():
    response = client.get("/comments")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_comment():
    response = client.patch("/comments/1", json={"content": "updatedcomment"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "content": "updatedcomment", "user_id": 1, "recipe_id": 1}

def test_delete_comment():
    response = client.delete("/comments/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Comment deleted successfully"}

# Test Like CRUD operations
def test_create_like():
    response = client.post("/likes", json={"user_id": 1, "recipe_id": 1})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "user_id": 1, "recipe_id": 1}

def test_get_like():
    response = client.get("/likes/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "user_id": 1, "recipe_id": 1}

def test_get_likes():
    response = client.get("/likes")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_delete_like():
    response = client.delete("/likes/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Like deleted successfully"}
