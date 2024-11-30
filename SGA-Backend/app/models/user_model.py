from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint, Column, Integer, String, Identity
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False, unique=True)
    email = Column(String(254), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    phone_number = Column(String(10), nullable=True)
    role = Column(String(10), nullable=False)

    # Relationships
    managed_store = relationship(
        "Store",
        back_populates="owner",
        cascade="all, delete-orphan",  # Enables cascade delete
        passive_deletes=True  # Enables database-side ON DELETE CASCADE
    )

    # Relationships
    grocery_lists = relationship("GroceryList", back_populates="user", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("LEN(phone_number) = 10", name="chk_phone_number_length"),
        CheckConstraint("role IN ('admin', 'manager', 'customer')", name="chk_role_values"),
    )
