from sqlalchemy import Column, Identity, Integer, String, Float, Date, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from app.database import Base
from app.schemas.product_schema import ProductStatus

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer,
                Identity(start=1, increment=1),
                primary_key=True,
                index=True)
    product_name = Column(String(100), nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    price = Column(Float(12,2), nullable=False)
    status = Column(SQLAlchemyEnum(ProductStatus), nullable=False)
    unit_of_measure = Column(String(20), nullable=False)
    ingredients = Column(String(255), nullable=False)
    price_valid_from = Column(Date, nullable=True)
    price_valid_to = Column(Date, nullable=False)

    # Foreign keys
    category_id = Column(Integer, ForeignKey('categories.category_id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=False)
    store_id = Column(Integer, ForeignKey('stores.store_id'), nullable=False)

    # Relationships
    category = relationship("Category", back_populates="products")
    department = relationship("Department", back_populates="products")
    store = relationship("Store", back_populates="products")