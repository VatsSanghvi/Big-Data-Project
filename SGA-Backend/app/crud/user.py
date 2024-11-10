from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from utils.authentication import hash_password

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
        role=user.role,
        phone_number=user.phone_number,
        address=user.address,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def update_user(db: Session, id: int, user: UserUpdate):
    db_user = get_user(db, id)
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def deactivate_user(db: Session, id: int):
    db_user = get_user(db, id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
