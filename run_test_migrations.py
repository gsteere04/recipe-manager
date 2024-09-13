from sqlalchemy import create_engine, text
from database import SQLALCHEMY_DATABASE_URL, Base
import models  # Import all your models

def setup_test_db():
    # Create a new engine for the test database
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    # Drop all tables
    Base.metadata.drop_all(bind=engine)

    # Create all tables
    Base.metadata.create_all(bind=engine)

    # Verify that tables are created
    with engine.connect() as connection:
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        tables = [row[0] for row in result]
        print(f"Tables after setup: {tables}")

if __name__ == "__main__":
    setup_test_db()
