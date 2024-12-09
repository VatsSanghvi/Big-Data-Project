from app.database import TestingSessionLocal
from app.schemas.user_schema import UserCreate, UserLogin, PasswordUpdate, UserUpdate
from app.crud import user_crud
from app.models import user_model,store_model, product_model, department_model, category_model, grocery_list_model, budget_model
from app.database import engine

# Setup a test database session
def get_test_db():
    user_model.Base.metadata.create_all(bind=engine)
    category_model.Base.metadata.create_all(bind=engine)
    product_model.Base.metadata.create_all(bind=engine)
    department_model.Base.metadata.create_all(bind=engine)
    store_model.Base.metadata.create_all(bind=engine)
    grocery_list_model.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

#-------------------------------------------------------------------------------------------------------------------------------
def test_register_user():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserCreate(
        first_name="Dev",
        last_name="Patel",
        email="dev12@gmail.com",
        password="password123",
        phone_number="1234567899",
        role="customer"
    )

    # Call the function
    inserted_user = user_crud.register_user(db=db, user=new_user)

    # Validate results
    assert user_crud.verify_password(
        plain_password="password123",
        hashed_password=inserted_user.password)
    assert user_crud.validate_email(
        email=inserted_user.email
    )
    assert user_crud.validate_phone_number(
        phone_number=inserted_user.phone_number
    )

#--------------------------------------------------------------------------------------------------------------------------
def test_login_user():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = UserLogin(
        email="dev@gmail.com",
        password="password123"
    )

    # Call the function
    login_user = user_crud.authenticate_user(db=db, email=new_user.email, password=new_user.password)
    assert user_crud.authenticate_user(db=db, email=login_user.email, password=login_user.password)

#--------------------------------------------------------------------------------------------------------------------------------------------
def test_logout_user():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock user ID
    user_id = 35 

    # Call the logout function
    response = user_crud.logout_user(db=db, user_id=user_id)

    # Validate the response
    assert response["message"] == "User logged out successfully"

#----------------------------------------------------------------------------------------------------------------------
def test_reset_password():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock valid email for password reset
    email = "dev1234@gmail.com"

    # Call the reset password function
    response = user_crud.reset_password(db=db, email=email)

    # Validate the response
    assert response["message"] == "Password reset email sent."

#--------------------------------------------------------------------------------------------------------------------
def test_update_password():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    new_user = PasswordUpdate(
        user_id=1,
        current_password="password123",
        new_password="password1234"
    )

    # Call the function
    updated_password = user_crud.update_password(db=db, user_id=new_user.user_id, current_password=new_user.current_password, new_password=new_user.new_password)

    # Validate results
    assert updated_password == True

#--------------------------------------------------------------------------------------------------------------------------------------------------
def test_update_user_profile():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock updated data
    updated_user = UserUpdate(
        user_id= 1,
        first_name="John",
        last_name="Pilgrim",
        phone_number="1234567899",
    )

    # Call the function
    updated_user_profile = user_crud.update_user_profile(db=db, user_id=updated_user.user_id, updates=updated_user)

    # Validate the updated user profile
    assert updated_user_profile.user_id == updated_user.user_id
    assert updated_user_profile.first_name == updated_user.first_name
    assert updated_user_profile.last_name == updated_user.last_name
    assert updated_user_profile.phone_number == updated_user.phone_number


def test_get_user_by_id():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    user_id = 1

    # Call the function
    user_by_id = user_crud.get_user_by_id(db, user_id=user_id)

    # Validate results
    assert user_by_id.user_id == user_by_id


def test_get_user_by_email():
    # Initialize the test database session
    db_generator = get_test_db()
    db = next(db_generator)

    # Mock data
    user_email = "dev123@gmail.com"

    # Call the function
    user_by_email = user_crud.get_user_by_email(db, email=user_email)

    # Validate results
    assert user_by_email.email == True

