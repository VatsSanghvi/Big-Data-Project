from sqlalchemy import Column, Identity, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=True)
    role = Column(String(20), nullable=False)

    # Relationships
    managed_store = relationship("Store", back_populates="manager")
