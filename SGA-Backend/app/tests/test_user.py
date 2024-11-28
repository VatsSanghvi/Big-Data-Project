from app.database import TestingSessionLocal
from app.schemas.user_schema import UserRegister, UserLogin
from app.crud import user_crud
from app.models import user_model,store_model, product_model, department_model, category_model, grocery_list_model
from app.database import engine

# Setup a test database session
def get_test_db():
    user_model.Base.metadata.create_all(bind=engine)
    category_model.Base.metadata.create_all(bind=engine)
    product_model.Base.metadata.create_all(bind=engine)
    department_model.Base.metadata.create_all(bind=engine)
    store_model.Base.metadata.create_all(bind=engine)
    grocerylist_model.Base.metadata.create_all(bind=engine)

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
        phone_number="1234567899",
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

def test_get_user_by_id():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserRegister(
        first_name="John",
        last_name="Pilgrim",
        email="johnpilgrim33@gmail.com",
        password="password123",
        phone_number="1234567899",
        role="customer"
    )

    # Insert a new user
    inserted_user = user_crud.register_user(db=db, user=new_user)

    # Call the function
    user_by_id = user_crud.get_user_by_id(db, user_id=inserted_user.user_id)

    # Validate results
    assert user_by_id.user_id == inserted_user.user_id


def test_get_user_by_email():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserRegister(
        first_name="John",
        last_name="Pilgrim",
        email="johnpilgrim33@gmail.com",
        password="password123",
        phone_number="1234567899",
        role="customer"
    )

    # Insert a new user
    inserted_user = user_crud.register_user(db=db, user=new_user)

    # Call the function
    user_by_email = user_crud.get_user_by_email(db, email=inserted_user.email)

    # Validate results
    assert user_by_email.email == inserted_user.email

def test_update_password():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserRegister(
        first_name="John",
        last_name="Pilgrim",
        email="johnpilgrim33@gmail.com",
        password="password123",
        phone_number="1234567899",
        role="customer"
    )

    # Insert a new user
    inserted_user = user_crud.register_user(db=db, user=new_user)

    # Call the function
    updated_password = user_crud.update_password(db=db, user_id=inserted_user.user_id, current_password="password123", new_password="password1234")

    # Validate results
    assert updated_password == True

def test_update_user_profile():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserRegister(
        first_name="John",
        last_name="Pilgrim",
        email="johnpilgrim33@gmail.com",
        password="password123",
        phone_number="1234567899",
        role="customer"
    )

    # Insert a new user
    inserted_user = user_crud.register_user(db=db, user=new_user)

    # Mock updated data
    updated_user = UserRegister(
        first_name="John",
        last_name="Pilgrim",
        email="johnpilgrim33@gmail.com",
        password="password123",
        phone_number="1234567899",
        role="customer"
    )

    # Call the function
    updated_user_profile = user_crud.update_user_profile(db=db, user_id=inserted_user.user_id, updates=updated_user)

    # Validate results
    assert updated_user_profile == True
    assert updated_user_profile.email == updated_user.email

test_login_user()
test_register_user()
test_get_user_by_id()
test_get_user_by_email()
test_update_password()
test_update_user_profile()


