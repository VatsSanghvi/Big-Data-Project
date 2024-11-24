from sqlalchemy import Column, Identity, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Store(Base):
    __tablename__ = "stores"
    
    store_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    store_name = Column(String(100), nullable=False)
    manager_id = Column(Integer, nullable=False)
    
    # Back reference to products
    departments = relationship("Department", back_populates="store")
    products = relationship("Product", back_populates="store")