from sqlalchemy import Column, Identity, Integer, String, DECIMAL, ForeignKey, Date
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Store(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    store_name = Column(String(100), nullable=False)
    location = Column(String(255), nullable=False)

    # Foreign key for manager
    fk_owner_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    fk_manager_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)

    # Relationships
    owner = relationship("User", back_populates="owned_store", foreign_keys=fk_owner_id)
    manager = relationship("User", back_populates="managed_store", foreign_keys=fk_manager_id)

    departments = relationship("Department", back_populates="store")
    products = relationship("Product", back_populates="store")
    prices = relationship("StorePrice", back_populates="store")

class StorePrice(Base):
    __tablename__ = "store_prices"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(DECIMAL(12, 2), nullable=False)
    quantity_limit = Column(Integer, nullable=True)
    matched_with_store = Column(String(100), nullable=True)

    # Foreign Keys
    store_id = Column(Integer, ForeignKey("stores.store_id", ondelete="CASCADE"))
    product_id = Column(Integer, ForeignKey("products.product_id"))

    # Add Check Constraint for price
    __table_args__ = (
        CheckConstraint("price >= 0", name="chk_store_price_positive"),  # Ensures price >= 0
    )

    # Relationships
    store = relationship("Store", back_populates="prices")
    product = relationship("Product", back_populates="store_prices")
    flyers = relationship("Flyer", back_populates="store_price")


class Flyer(Base):
    __tablename__ = "flyers"

    flyer_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    flyer_url = Column(String(255), nullable=False)

    # Foreign Keys
    store_price_id = Column(Integer, ForeignKey("store_prices.id", ondelete="CASCADE"))

    # Relationships
    store_price = relationship("StorePrice", back_populates="flyers")