# Recipe Manager API

This is a FastAPI-based Recipe Manager API that allows users to create, read, update, and delete recipes, comments, and likes.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Setup

1. Clone the repository:
   ```
   git clone (ssh key here)
   cd recipe-manager
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate 
    # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your PostgreSQL database and update the database URL in `database.py`:
   ```python:database.py
   startLine: 5
   endLine: 5
   ```

5. Run the database migrations:
   ```
   alembic upgrade head
   ```

## Running the Application

To start the FastAPI server, run:
```
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.

## Running Tests

To run the tests, follow these steps:

1. Ensure you have a separate test database set up. Update the test database URL in `test.py`:
   ```python:test.py
   startLine: 10
   endLine: 10
   ```

2. Run the tests using pytest:
   ```
   pytest test.py
   ```

This will run all the tests, including unit tests and the integration test.

## API Endpoints

The API provides the following endpoints:

- Users: CRUD operations for users
- Recipes: CRUD operations for recipes
- Comments: CRUD operations for comments
- Likes: CRUD operations for likes

For detailed information about the available endpoints and their usage, refer to the API documentation at `http://localhost:8000/docs` when the server is running.

## API Documentation

The API documentation is available at:
```
http://127.0.0.1:8000/docs
```

This documentation is generated using Swagger UI.

## API Documentation

The API documentation is available at:
```
http://127.0.0.1:8000/docs
```

This documentation is generated using Swagger UI.
