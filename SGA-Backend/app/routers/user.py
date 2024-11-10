from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user as crud_user
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db=db, user=user)

@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{id}", response_model=UserResponse)
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return crud_user.update_user(db=db, id=id, user=user)

@router.delete("/{id}", response_model=UserResponse)
def delete_user(id: int, db: Session = Depends(get_db)):
    return crud_user.delete_user(db=db, id=id)
