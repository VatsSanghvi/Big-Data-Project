from sqlalchemy import Column, Integer, String, Identity, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class GroceryList(Base):
    __tablename__ = "grocery_lists"
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    name = Column(String)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)

    # Relationships
    items = relationship("GroceryItem", back_populates="grocery_list", cascade="all, delete")
    user = relationship("User", back_populates="grocery_lists")

class GroceryItem(Base):
    __tablename__ = "grocery_items"
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    name = Column(String)
    category = Column(String)

    # Foreign Keys
    grocery_list_id = Column(Integer, ForeignKey("grocery_lists.id"))

    # Relationships
    grocery_list = relationship("GroceryList", back_populates="items")