from sqlalchemy import Column, ForeignKey, Identity, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    department_name = Column(String(100), nullable=False)

    # Foreign keys
    fk_store_id = Column(Integer, ForeignKey("stores.store_id"))

    # Relationships
    store = relationship("Store", back_populates="departments")
    categories = relationship("Category", back_populates="department")
    products = relationship("Product", back_populates="department")
