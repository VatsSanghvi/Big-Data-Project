from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.utils.password_reset_email import send_password_reset_email
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.utils.authentication import hash_password
from passlib.context import CryptContext
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db: Session, user: UserCreate):
    """
    Register a new user in the database

    :param db: SQLAlchemy database session
    :param user: The user data to register
    """
    # Validate email
    validate_email(user.email)

    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ValueError(f"Email {user.email} is already registered.")

    # Validate phone number
    validate_phone_number(user.phone_number)

    # Proceed with user creation
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
        phone_number=user.phone_number,
        role=user.role
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to create user: {str(e)}") from e

def logout_user(db: Session, user_id: int):
    """
    Log out a user by their user_id.
    
    This function would typically invalidate a session or token. 
    For simplicity, we'll assume the logout action is just a basic check for existence.
    
    :param db: SQLAlchemy database session
    :param user_id: The user's ID to log out
    :return: A success message if the user exists and is logged out
    """
    # Check if the user exists in the database
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise ValueError(f"User with ID {user_id} not found.")
    
    # For simplicity, we're not invalidating a session or token here
    # But if you had a session or token, you could invalidate it here.
    
    return {"message": "User logged out successfully"}


def authenticate_user(db: Session, email: str, password: str):
    """
    Authenticate a user by email and password

    :param db: SQLAlchemy database session
    :param email: The user's email
    :param password: The user's password
    """
    user = get_user_by_email(db, email)

    if not user:
        raise ValueError("User not found")
    if not verify_password(password, user.password):
        raise ValueError("Invalid email or password")
    return user

def get_user_by_id(db: Session, user_id: int):
    """
    Get a user by their ID
    :param db: SQLAlchemy database session
    :param user_id: The user's ID
    :return: The user object
    """
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise ValueError(f"User with ID {user_id} not found.")
    return user

def get_user_by_email(db: Session, email: str):
    """
    Get a user by their email
    :param db: SQLAlchemy database session
    :param email: The user's email
    :return: The user object
    """
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise ValueError(f"User with email {email} not found.")
    return user

def update_password(db: Session, user_id: int, current_password: str, new_password: str):
    """
    Recover a user's password
    :param db: SQLAlchemy database session
    :param user_id: The user's ID
    :param current_password: The user's current password
    :param new_password: The user's new password
    :return: True if the password was updated, False otherwise
    """
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(f"User with ID {user_id} not found.")

    if not verify_password(current_password, user.password):
        raise ValueError("Invalid password")

    try:
        user.password = new_password
        db.commit()
        return True
    except:
        db.rollback()
        raise ValueError("Failed to update password")

def update_user_role(db: Session, user_id: int, role: str):
    """
    Update a user's profile
    :param db: SQLAlchemy database session
    :param user_id: The user's ID
    :param role: The user's role
    :return: The updated user object
    """
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise ValueError(f"User with ID {user_id} not found.")

    # Apply updates
    setattr(user, "role", role)

    try:
        db.commit()
        db.refresh(user)
        return UserResponse.model_validate(user)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update product: {str(e)}") from e

def update_user_profile(db: Session, user_id: int, updates: UserUpdate):
    """
    Update a user's profile
    :param db: SQLAlchemy database session
    :param user_id: The user's ID
    :param updates: The user's updated data
    :return: The updated user object
    """
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise ValueError(f"User with ID {user_id} not found.")

    # Apply updates
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    try:
        db.commit()
        db.refresh(user)
        return UserResponse.model_validate(user)
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Failed to update product: {str(e)}") from e

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password"""
    return plain_password, hashed_password

def validate_email(email: str):
    """
    Validates if an email is from an allowed domain.

    :param email: The email address to validate.
    :raises ValueError: If the email domain is not allowed or the email is invalid.
    """

    # Validate the basic email format
    email_regex = r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$"
    if not re.match(email_regex, email):
        raise ValueError("Invalid email")
    return True

def validate_phone_number(phone_number: str):
    if not phone_number.isdigit() or len(phone_number) != 10:
        raise ValueError("Phone number must be exactly 10 digits.")
    return True

def reset_password(db: Session, email: str):
    """
    Initiates the password reset process by sending a reset link to the user's email.
    
    :param db: SQLAlchemy database session
    :param email: The email of the user who requests a password reset
    :return: A success message if the email is sent
    """
    # Find the user by email
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise ValueError("No user found with the provided email.")

    # Simulate sending password reset email (you can replace this with actual email-sending code)
    send_password_reset_email(email)

    return {"message": "Password reset email sent."}