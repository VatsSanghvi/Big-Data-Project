from sqlalchemy import Column, Identity, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Store(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    store_name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)

    # Foreign key for manager
    fk_manager_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # Relationships
    manager = relationship("User", back_populates="managed_store", uselist=False, cascade="all, delete")
    departments = relationship("Department", back_populates="store")
    products = relationship("Product", back_populates="store")

