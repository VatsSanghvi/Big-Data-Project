
from sqlalchemy.orm import sessionmaker
from app.database import TestingSessionLocal
from app.schemas.user_schema import UserRegister, UserRole
from app.crud import user_crud

# Setup a test database session
def get_test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Testing the function
def test_register_user():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserRegister(
        first_name="John",
        last_name="Doe",
        email="johndoe@gmail.com",
        password="password123",
        phone_number="1234567890",
        role=UserRole.ADMIN
    )

    # Call the function
    inserted_user = user_crud.register_user(db=db, user=new_user)

    # Validate results
    assert inserted_user.email == "johndoe@gmail.com"
    assert user_crud.verify_password(
        plain_password="password123",
        hashed_password=inserted_user.password)
    assert inserted_user.role == UserRole.ADMIN

test_register_user()


