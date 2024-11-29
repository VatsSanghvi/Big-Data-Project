from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserRegister,UserUpdate, UserResponse
from app.utils.authentication import hash_password
from passlib.context import CryptContext
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db: Session, user: UserRegister) -> User:
    """
    Register a new user in the database

    :param db: SQLAlchemy database session
    :param user: The user data to register
    """
    # Validate email
    validate_email_domain(user.email)

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
        password=hash_password(user.password),
        phone_number=user.phone_number,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def authenticate_user(db: Session, email: str, password: str):
    """
    Authenticate a user by email and password

    :param db: SQLAlchemy database session
    :param email: The user's email
    :param password: The user's password
    """
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password) and validate_email_domain(user.email) and validate_phone_number(user.phone_number):
        return None
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
    Update a user's password
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
        return False

    try:
        user.password = pwd_context.hash(new_password)
        db.commit()
        return True
    except:
        db.rollback()
        raise ValueError("Failed to update password")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password"""
    return pwd_context.verify(plain_password, hashed_password)

def validate_email_domain(email: str):
    """
    Validates if an email is from an allowed domain.

    :param email: The email address to validate.
    :raises ValueError: If the email domain is not allowed or the email is invalid.
    """
    allowed_domains = ["gmail.com", "hotmail.com", "yahoo.com", "icloud.com"]

    # Validate the basic email format
    email_regex = r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$"
    if not re.match(email_regex, email):
        raise ValueError("Invalid email")

    # Extract domain and check if it's allowed
    domain = email.split("@")[-1]
    if domain not in allowed_domains:
        raise ValueError(f"Email domain '{domain}' is not supported. Allowed domains: {', '.join(allowed_domains)}.")

def validate_phone_number(phone_number: str):
    if not phone_number.isdigit() or len(phone_number) != 10:
        raise ValueError("Phone number must be exactly 10 digits.")


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


