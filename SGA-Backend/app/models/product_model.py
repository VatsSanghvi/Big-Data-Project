from sqlalchemy import (
    Column,
    Integer,
    Identity,
    DECIMAL,
    String,
    ForeignKey,
    CheckConstraint,
    DateTime
)
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    product_id = Column(
        Integer,
        Identity(start=1, increment=1),
        primary_key=True,
        index=True
    )
    product_name = Column(String(100), nullable=False, unique=True)
    stock_quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(12, 2), nullable=False)
    status = Column(
        String(10),
        nullable=False,
        default="In Stock"
    )  # Matches CHECK(status IN ('In Stock', 'Out Of Stock'))

    # Foreign keys
    fk_category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=True)
    fk_department_id = Column(Integer, ForeignKey("departments.department_id"), nullable=True)
    fk_store_id = Column(Integer, ForeignKey("stores.store_id", ondelete="CASCADE"), nullable=True)

    # Add Check Constraints for price and status
    __table_args__ = (
        CheckConstraint("price >= 0", name="chk_price_positive"),  # Ensures price >= 0
        CheckConstraint(
            "status IN ('In Stock', 'Out Of Stock')",
            name="chk_status_valid"
        ),  # Ensures valid status values
    )

    # Relationships
    category = relationship("Category", back_populates="products")
    department = relationship("Department", back_populates="products")
    store = relationship("Store", back_populates="products")
    store_prices = relationship("StorePrice", back_populates="product")
    grocery_item = relationship("GroceryItem", back_populates="product")

class SearchLog(Base):
    __tablename__ = "search_logs"

    search_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    search_term = Column(String(100), nullable=False)
    search_date = Column(DateTime, default=datetime.now)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="searches")

