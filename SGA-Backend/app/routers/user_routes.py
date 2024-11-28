from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from app.crud import user_crud
from app.schemas.user_schema import UserLogin, UserRegister, UserUpdate, PasswordUpdate, PasswordReset
from app.schemas.user_schema import  UserResponse
from app.database import SessionLocal
# from app.utils.email_service import send_password_reset_email

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        return user_crud.register_user(db=db, user=user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=UserResponse)
def login(request: UserLogin, db: Session = Depends(get_db)):
    try:
        return user_crud.authenticate_user(db, request.email, request.password)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

@router.put("/profile")
async def update_profile(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
):
    updated_user = user_crud.update_user_profile(db, user_id, user_data)
    return updated_user

@router.put("/password")
async def update_password(
    user_id: int,
    password_data: PasswordUpdate,
    db: Session = Depends(get_db)
):
    current_user = user_crud.get_user_by_id(db, user_id)

    if not user_crud.update_password(
        db,
        current_user.user_id,
        password_data.current_password,
        password_data.new_password
    ):
        raise HTTPException(status_code=400, detail="Invalid current password")
    return {"message": "Password updated successfully"}

# @router.post("/password-reset")
# async def request_password_reset(
#     reset_data: PasswordReset,
#     background_tasks: BackgroundTasks,
# ):
#     # Send email in background to not block the response
#     background_tasks.add_task(
#         send_password_reset_email,
#         reset_data.email,
#     )
#     # Always return success to prevent email enumeration
#     return {"message": "If the email exists, a password reset link has been sent"}