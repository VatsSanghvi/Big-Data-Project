from sqlalchemy import Column, ForeignKey, Integer, Identity, String
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"
    
    category_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    category_name = Column(String(100), nullable=False)
    
    # Foreign Keys
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)
    
    # Relationships - Reference the class names
    department = relationship("Department", back_populates="departments")