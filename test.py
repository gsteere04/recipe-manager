from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main2 import app, get_db

client = TestClient(app)

mock_users = [
    {"id": 1, "username": "user1"},
    {"id": 2, "username": "user2"},
]

mock_recipes = [
    {"id": 1, "name": "Recipe 1", "ingredients": "Ingredients 1", "instructions": "Instructions 1", "user_id": 1},
    {"id": 2, "name": "Recipe 2", "ingredients": "Ingredients 2", "instructions": "Instructions 2", "user_id": 2},
]

@patch("main2.crud.get_users")
def test_get_users(mock_get_users):
    mock_get_users.return_value = mock_users

    response = client.get("/users")

    assert response.status_code == 200

    assert response.json() == mock_users

@patch("main2.crud.get_user")
def test_get_user(mock_get_user):
    mock_user = {"id": 1, "username": "user1"}
    mock_get_user.return_value = mock_user

    response = client.get("/users/1")

    assert response.status_code == 200

    assert response.json() == mock_user

@patch("main2.crud.create_user")
def test_create_user(mock_create_user):
    mock_create_user.return_value = {"id": 1, "username": "user1"}

    response = client.post("/users", json={"username": "user1"})

    assert response.status_code == 200

    assert "id" in response.json()
    assert response.json()["username"] == "user1"

@patch("main2.crud.updated_user")
def test_update_user(mock_update_user):
    mock_update_user.return_value = {"id": 1, "username": "updated_user"}

    response = client.patch("/users/1", json={"username": "updated_user"})

    assert response.status_code == 200

    assert "id" in response.json()
    assert response.json()["username"] == "updated_user"

@patch("main2.crud.delete_user")
def test_delete_user(mock_delete_user):
    mock_delete_user.return_value = True

    response = client.delete("/users/1")

    assert response.status_code == 200

    assert response.json()["message"] == "User deleted successfully"

@patch("main2.crud.get_recipes")
def test_get_recipes(mock_get_recipes):
    mock_get_recipes.return_value = mock_recipes

    response = client.get("/recipes")

    assert response.status_code == 200

    assert response.json() == mock_recipes

@patch("main2.crud.get_recipe")
def test_get_recipe(mock_get_recipe):
    mock_recipe = {"id": 1, "name": "Recipe 1", "ingredients": "Ingredients 1", "instructions": "Instructions 1", "user_id": 1}
    mock_get_recipe.return_value = mock_recipe

    response = client.get("/recipes/1")

    assert response.status_code == 200

    assert response.json() == mock_recipe

@patch("main2.crud.create_recipe")
def test_create_recipe(mock_create_recipe):
    mock_create_recipe.return_value = {"id": 1, "name": "Recipe 1", "ingredients": "Ingredients 1", "instructions": "Instructions 1", "user_id": 1}

    response = client.post("/recipes", json={"name": "Recipe 1", "ingredients": "Ingredients 1", "instructions": "Instructions 1", "user_id": 1})

    assert response.status_code == 200

    assert "id" in response.json()
    assert response.json()["name"] == "Recipe 1"

@patch("main2.crud.update_recipe")
def test_update_recipe(mock_update_recipe):
    mock_update_recipe.return_value = {"id": 1, "name": "Updated Recipe", "ingredients": "Updated Ingredients", "instructions": "Updated Instructions", "user_id": 1}

    response = client.patch("/recipes/1", json={"name": "Updated Recipe", "ingredients": "Updated Ingredients", "instructions": "Updated Instructions", "user_id": 1})

    assert response.status_code == 200

    assert "id" in response.json()
    assert response.json()["name"] == "Updated Recipe"

@patch("main2.crud.delete_recipe")
def test_delete_recipe(mock_delete_recipe):
    mock_delete_recipe.return_value = True

    response = client.delete("/recipes/1")

    assert response.status_code == 200

    assert response.json()["message"] == "Recipe deleted successfully"
