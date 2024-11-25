from app.database import TestingSessionLocal
from app.schemas.user_schema import UserRegister, UserLogin
from app.crud import user_crud
from app.models import user_model,category_model, department_model, product_model, store_model
from app.database import engine

# Setup a test database session
def get_test_db():
    user_model.Base.metadata.create_all(bind=engine)
    #department_model.Base.metadata.create_all(bind=engine)
    #category_model.Base.metadata.create_all(bind=engine)
    store_model.Base.metadata.create_all(bind=engine)
    #product_model.Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_login_user():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserLogin(
        email="johnpilgrim@gmail.com",
        password="password123"
    )

    # Call the function
    login_user = user_crud.authenticate_user(db=db, email=new_user.email, password=new_user.password)
    assert user_crud.authenticate_user(db=db, email=login_user.email, password=login_user.password)

def test_register_user():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserRegister(
        first_name="John",
        last_name="Pilgrim",
        email="johnpilgrim33@gmail.com",
        password="password123",
        phone_number="123456789",
        role="admin"
    )

    # Call the function
    inserted_user = user_crud.register_user(db=db, user=new_user)

    # Validate results
    assert user_crud.verify_password(
        plain_password="password123",
        hashed_password=inserted_user.password)
    assert user_crud.validate_email_domain(
        email=inserted_user.email
    )
    assert user_crud.validate_phone_number(
        phone_number=inserted_user.phone_number
    )

test_login_user()
test_register_user()


