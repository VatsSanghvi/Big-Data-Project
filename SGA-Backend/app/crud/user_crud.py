from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserRegister
from app.utils.authentication import hash_password
from passlib.context import CryptContext
import re


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db: Session, user: UserRegister) -> User:
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
    """Authenticate a user by email and password"""
    user_obj = db.query(User).filter(User.email == email).first()
    user = User(
        user_id=user_obj.user_id,
        first_name=user_obj.first_name,
        last_name=user_obj.last_name,
        email=user_obj.email,
        password=user_obj.password,
        phone_number=user_obj.phone_number,
        role=user_obj.role
    )
    if not user:
        return None
    if not verify_password(password, user.password) and validate_email_domain(user.email) and validate_phone_number(user.phone_number):
        return None
    return user

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
