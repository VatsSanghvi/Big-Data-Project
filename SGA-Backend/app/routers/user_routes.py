from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import user_crud
from app.schemas.user_schema import UserResponse, UserLogin, UserResponse
from app.schemas.user_schema import  UserResponse
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user: UserResponse, db: Session = Depends(get_db)):
    try:
        return user_crud.register(db=db, user=user)
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