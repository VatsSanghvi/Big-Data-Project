from sqlalchemy import Column, Integer, String, Identity, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.database import Base

class GroceryList(Base):
    __tablename__ = "grocery_lists"
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    total_spent = Column(DECIMAL(10, 2), default=0)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # Relationships
    items = relationship("GroceryItem", back_populates="grocery_list", cascade="all, delete-orphan")
    user = relationship("User", back_populates="grocery_lists")

class GroceryItem(Base):
    __tablename__ = "grocery_items"

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)

    # Foreign Keys
    grocery_list_id = Column(Integer, ForeignKey("grocery_lists.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)

    # Relationships
    grocery_list = relationship("GroceryList", back_populates="items")
    product = relationship("Product", back_populates="grocery_item")