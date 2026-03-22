from database import SessionLocal
from sqlalchemy import text
from models import User, Note

#testing connection
def test_database_connection():
    db = SessionLocal()

    try:
        result = db.execute(text("SELECT 1"))
        value = result.scalar()

        assert value == 1

    finally:
        db.close()

def test_create_user():
    db = SessionLocal()

    try:
        #1. Create new user
        new_user = User(name = "Test User", email = "test@example.com")
        db.add(new_user)
        db.commit()

        # query the user back
        user_in_db = db.query(User).filter_by(email = "test@example.com").first()

        #assertions
        assert user_in_db is not None
        assert user_in_db.name  == "Test User"
        assert user_in_db.email == "test@example.com"
    finally:
        db.close()