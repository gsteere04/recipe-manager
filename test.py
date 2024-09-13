import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from main import app
from run_test_migrations import setup_test_db

# Use a different database for testing
TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/recipe_browser_test"

# Create a new engine instance for the test database
test_engine = create_engine(TEST_DATABASE_URL)

# Create a TestingSessionLocal class
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

@pytest.fixture(scope="function", autouse=True)
def setup_test_database():
    Base.metadata.drop_all(bind=test_engine)
    setup_test_db()
    yield
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture(scope="function")
def client():
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    del app.dependency_overrides[get_db]

def test_create_user(client):
    response = client.post("/users", json={"username": "testuser"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_get_user(client):
    # First, create a user
    create_response = client.post("/users", json={"username": "testuser"})
    user_id = create_response.json()["id"]

    # Then, get the user
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["username"] == "testuser"

def test_create_recipe(client):
    # First, create a user
    user_response = client.post("/users", json={"username": "testuser"})
    user_id = user_response.json()["id"]

    # Then, create a recipe
    recipe_response = client.post("/recipes", json={
        "title": "Test Recipe",
        "description": "This is a test recipe",
        "user_id": user_id
    })
    assert recipe_response.status_code == 200
    data = recipe_response.json()
    assert data["title"] == "Test Recipe"
    assert data["description"] == "This is a test recipe"
    assert "id" in data

def test_get_recipe(client):
    # First, create a user and a recipe
    user_response = client.post("/users", json={"username": "testuser"})
    user_id = user_response.json()["id"]
    recipe_response = client.post("/recipes", json={
        "title": "Test Recipe",
        "description": "This is a test recipe",
        "user_id": user_id
    })
    recipe_id = recipe_response.json()["id"]

    # Then, get the recipe
    get_response = client.get(f"/recipes/{recipe_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Test Recipe"
    assert get_response.json()["description"] == "This is a test recipe"

def test_update_recipe(client):
    # First, create a user and a recipe
    user_response = client.post("/users", json={"username": "testuser"})
    user_id = user_response.json()["id"]
    recipe_response = client.post("/recipes", json={
        "title": "Test Recipe",
        "description": "This is a test recipe",
        "user_id": user_id
    })
    recipe_id = recipe_response.json()["id"]

    # Then, update the recipe
    update_response = client.put(f"/recipes/{recipe_id}", json={
        "instructions": "Step 1: Do this. Step 2: Do that.",
        "ingredients": "Ingredient 1, Ingredient 2"
    })
    assert update_response.status_code == 200
    assert update_response.json()["instructions"] == "Step 1: Do this. Step 2: Do that."
    assert update_response.json()["ingredients"] == "Ingredient 1, Ingredient 2"
    # The title and description should remain unchanged
    assert update_response.json()["title"] == "Test Recipe"
    assert update_response.json()["description"] == "This is a test recipe"

def test_delete_recipe(client):
    # First, create a user and a recipe
    user_response = client.post("/users", json={"username": "testuser"})
    user_id = user_response.json()["id"]
    recipe_response = client.post("/recipes", json={
        "title": "Test Recipe",
        "description": "This is a test recipe",
        "user_id": user_id
    })
    recipe_id = recipe_response.json()["id"]

    # Then, delete the recipe
    delete_response = client.delete(f"/recipes/{recipe_id}")
    assert delete_response.status_code == 200

    # Verify the recipe is deleted
    get_response = client.get(f"/recipes/{recipe_id}")
    assert get_response.status_code == 404

def test_create_comment(client):
    # First, create a user and a recipe
    user_response = client.post("/users", json={"username": "testuser"})
    user_id = user_response.json()["id"]
    recipe_response = client.post("/recipes", json={
        "title": "Test Recipe",
        "description": "This is a test recipe",
        "user_id": user_id
    })
    recipe_id = recipe_response.json()["id"]

    # Then, create a comment
    comment_response = client.post("/comments", json={
        "content": "Great recipe!",
        "user_id": user_id,
        "recipe_id": recipe_id
    })
    assert comment_response.status_code == 200
    assert comment_response.json()["content"] == "Great recipe!"

def test_create_like(client):
    # First, create a user and a recipe
    user_response = client.post("/users", json={"username": "testuser"})
    user_id = user_response.json()["id"]
    recipe_response = client.post("/recipes", json={
        "title": "Test Recipe",
        "description": "This is a test recipe",
        "user_id": user_id
    })
    recipe_id = recipe_response.json()["id"]

    # Then, create a like
    like_response = client.post("/likes", json={
        "user_id": user_id,
        "recipe_id": recipe_id
    })
    assert like_response.status_code == 200

def test_error_handling(client):
    # Try to get a non-existent user
    non_existent_user_response = client.get("/users/9999")
    assert non_existent_user_response.status_code == 404

    # Try to create a recipe with a non-existent user
    invalid_recipe_response = client.post("/recipes", json={
        "title": "Invalid Recipe",
        "description": "This is an invalid recipe",
        "user_id": 9999
    })
    assert invalid_recipe_response.status_code == 404  # or 400, depending on your error handling

    # Try to create a comment for a non-existent recipe
    user_response = client.post("/users", json={"username": "testuser"})
    user_id = user_response.json()["id"]
    invalid_comment_response = client.post("/comments", json={
        "content": "Invalid comment",
        "user_id": user_id,
        "recipe_id": 9999
    })
    assert invalid_comment_response.status_code == 404

    # Try to like a non-existent recipe
    invalid_like_response = client.post("/likes", json={
        "user_id": user_id,
        "recipe_id": 9999
    })
    assert invalid_like_response.status_code == 404

def test_integrated_flow(client):
    # Create a user
    user_response = client.post("/users", json={"username": "testuser"})
    assert user_response.status_code == 200
    user_id = user_response.json()["id"]

    # Create a recipe
    recipe_response = client.post("/recipes", json={
        "title": "Test Recipe",
        "description": "This is a test recipe",
        "user_id": user_id
    })
    assert recipe_response.status_code == 200
    recipe_id = recipe_response.json()["id"]

    # Create a comment
    comment_response = client.post("/comments", json={
        "content": "Great recipe!",
        "user_id": user_id,
        "recipe_id": recipe_id
    })
    assert comment_response.status_code == 200
    comment_id = comment_response.json()["id"]

    # Create a like
    like_response = client.post("/likes", json={
        "user_id": user_id,
        "recipe_id": recipe_id
    })
    assert like_response.status_code == 200

    # Get user's comments
    user_comments_response = client.get(f"/users/{user_id}/comments")
    assert user_comments_response.status_code == 200
    assert len(user_comments_response.json()) == 1
    assert user_comments_response.json()[0]["id"] == comment_id

    # Get user's liked recipes
    user_likes_response = client.get(f"/users/{user_id}/liked_recipes")
    assert user_likes_response.status_code == 200
    assert len(user_likes_response.json()) == 1
    assert user_likes_response.json()[0]["id"] == recipe_id

    # Update the recipe
    update_recipe_response = client.put(f"/recipes/{recipe_id}", json={
        "instructions": "Updated Step 1, Updated Step 2",
        "ingredients": "Updated Ingredient 1, Updated Ingredient 2"
    })
    assert update_recipe_response.status_code == 200

    # Delete the comment
    delete_comment_response = client.delete(f"/comments/{comment_id}")
    assert delete_comment_response.status_code == 200

    # Delete the recipe
    delete_recipe_response = client.delete(f"/recipes/{recipe_id}")
    assert delete_recipe_response.status_code == 200

    # Delete the user
    delete_user_response = client.delete(f"/users/{user_id}")
    assert delete_user_response.status_code == 200

    # Verify user is deleted
    get_deleted_user_response = client.get(f"/users/{user_id}")
    assert get_deleted_user_response.status_code == 404
