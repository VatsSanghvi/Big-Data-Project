from typing import List
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserRegister, UserResponse
from app.utils.authentication import hash_password
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db: Session, user: UserRegister) -> UserResponse:
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
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password"""
    return pwd_context.verify(plain_password, hashed_password)

def validate_email_domain(email: str):
    allowed_domains = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@icloud.com"]
    if not any(email.endswith(domain) for domain in allowed_domains):
        raise ValueError("Email must be from a supported domain.")

def validate_phone_number(phone_number: str):
    if not phone_number.isdigit() or len(phone_number) != 10:
        raise ValueError("Phone number must be exactly 10 digits.")
