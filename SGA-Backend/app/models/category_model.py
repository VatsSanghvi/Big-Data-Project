from sqlalchemy import Column, ForeignKey, Integer, Identity, String
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    category_name = Column(String(100), nullable=False)

    # Foreign Keys
    fk_department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)

    # Relationships
    department = relationship("Department", back_populates="categories")
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")
