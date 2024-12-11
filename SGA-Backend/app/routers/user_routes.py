from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import user_crud
from app.schemas.user_schema import UserLogin, UserCreate, UserUpdate, PasswordUpdate, PasswordReset
from app.schemas.user_schema import  UserResponse
from app.database import SessionLocal
from app.utils.base_response import BaseResponse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=BaseResponse[UserResponse])
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        registered_user = user_crud.register_user(db=db, user=user)
        return BaseResponse.success_response(
            data=registered_user,
            message="Register successful"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.post("/login", response_model=BaseResponse[UserResponse])
def login(request: UserLogin, db: Session = Depends(get_db)):
    try:
        user = user_crud.authenticate_user(db, request.email, request.password)
        return BaseResponse.success_response(
            data=user,
            message="Login successful"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.put("/profile/{user_id}", response_model=BaseResponse[UserResponse])
async def update_profile(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
):
    try:
        updated_user = user_crud.update_user_profile(db, user_id, user_data)
        return BaseResponse.success_response(
            data=updated_user,
            message="Profile updated successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.post("/send-email", response_model=BaseResponse)
async def request_password_reset(passwordReset: PasswordReset):
    message = MIMEMultipart("alternative")
    message["From"] = passwordReset.sender_email
    message["To"] = passwordReset.to_email
    message["Subject"] = "Recover your account"
    recovery_link = f"http://localhost:5173/reset-password/{passwordReset.to_email}"
    text = f"Please use the following link to recover your account: {recovery_link}"
    part = MIMEText(text, "plain")
    message.attach(part)

    try:
        part = MIMEText(text, "plain")
        message.attach(part)
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.set_debuglevel(1)
        server.esmtp_features['auth'] = 'LOGIN PLAIN'
        server.login(MAIL_USERNAME, MAIL_PASSWORD)
        server.sendmail(passwordReset.sender_email, passwordReset.to_email, message.as_string())

        return BaseResponse.success_response(
            message="Email sent successfully"
        )

    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

@router.put("/reset-password/{email}", response_model=BaseResponse)
async def reset_password(
    email: str,
    password_data: PasswordUpdate,
    db: Session = Depends(get_db)
):
    try:
        current_user = user_crud.get_user_by_email(db, email)
        updated_password = user_crud.reset_password(
            db,
            current_user.user_id,
            password_data.current_password,
            password_data.new_password
        )
        return BaseResponse.success_response(
            data=updated_password,
            message="Password updated successfully"
        )
    except Exception as e:
        return BaseResponse.error_response(
            message=str(e)
        )

