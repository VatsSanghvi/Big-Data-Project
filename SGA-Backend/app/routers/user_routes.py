from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.crud import user_crud
from app.schemas.user_schema import UserLogin, UserCreate, UserUpdate, PasswordUpdate, PasswordReset
from app.schemas.user_schema import  UserResponse
from app.database import SessionLocal
from app.utils.base_response import BaseResponse
# from app.utils.email_service import send_password_reset_email

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

@router.put("/password", response_model=BaseResponse[UserResponse])
async def update_password(
    user_id: int,
    password_data: PasswordUpdate,
    db: Session = Depends(get_db)
):
    try:
        current_user = user_crud.get_user_by_id(db, user_id)
        updated_password = user_crud.update_password(
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

# @router.post("/password-reset", response_model=BaseResponse)
# async def request_password_reset(
#     reset_data: PasswordReset,
#     background_tasks: BackgroundTasks,
# ):
#     # Send email in background to not block the response
#     try:
#         background_tasks.add_task(
#             send_password_reset_email,
#             reset_data.email,
#         )
#         return BaseResponse.success_response(
#             message="Password reset email sent successfully"
#         )
#     except Exception as e:
#         return BaseResponse.error_response(
#             message=str(e)
#         )
