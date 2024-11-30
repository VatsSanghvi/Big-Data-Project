from sqlalchemy import (
    Column,
    Integer,
    Identity,
    DECIMAL,
    Date,
    String,
    Text,
    ForeignKey,
    CheckConstraint
)
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(
        Integer,
        Identity(start=1, increment=1),
        primary_key=True,
        index=True
    )
    product_name = Column(String(100), nullable=False, unique=True)  # Enforces uniqueness
    stock_quantity = Column(Integer, nullable=False, default=0)  # Matches DEFAULT 0
    price = Column(DECIMAL(12, 2), nullable=False)  # Matches DECIMAL(12, 2)
    status = Column(
        String(10),
        nullable=False,
        default="In Stock"
    )  # Matches CHECK(status IN ('In Stock', 'Out Of Stock'))
    unit_of_measure = Column(String(20), nullable=False, default="unit")  # Matches DEFAULT 'unit'
    ingredients = Column(Text, nullable=True)  # Matches TEXT type
    price_valid_from = Column(Date, nullable=True)
    price_valid_to = Column(Date, nullable=True)

    # Foreign keys with proper ON DELETE SET NULL
    fk_category_id = Column(
        Integer,
        ForeignKey("categories.category_id", ondelete="SET NULL"),
        nullable=True
    )
    fk_department_id = Column(
        Integer,
        ForeignKey("departments.department_id", ondelete="SET NULL"),
        nullable=True
    )
    fk_store_id = Column(
        Integer,
        ForeignKey("stores.store_id", ondelete="SET NULL"),
        nullable=True
    )

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
