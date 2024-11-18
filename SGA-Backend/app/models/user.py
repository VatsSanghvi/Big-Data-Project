from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum
from app.database import Base
from app.schemas.user import UserRole

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False)