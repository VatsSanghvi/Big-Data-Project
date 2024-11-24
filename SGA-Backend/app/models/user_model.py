from sqlalchemy import Column, Identity, Integer, String, Enum as SQLAlchemyEnum
from app.database import Base
from app.schemas.user_schema import UserRole

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer,
                Identity(start=1, increment=1), 
                primary_key=True, 
                index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=True)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False)