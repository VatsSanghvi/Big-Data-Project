from sqlalchemy import Column, Identity, Integer, String, DECIMAL, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Store(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    store_name = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)

    # Foreign key for manager
    fk_manager_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)

    # Relationships
    manager = relationship("User", back_populates="managed_store")
    departments = relationship("Department", back_populates="store")
    products = relationship("Product", back_populates="store")
    prices = relationship("StorePrice", back_populates="store")

class StorePrice(Base):
    __tablename__ = "store_prices"
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.store_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    price = Column(DECIMAL(10, 2))
    price_valid_from = Column(DateTime)
    price_valid_until = Column(DateTime)
    quantity_limit = Column(Integer, nullable=True)
    is_on_sale = Column(Boolean, default=False)
    store = relationship("Store", back_populates="prices")
    product = relationship("Product", back_populates="store_prices")