from sqlalchemy import Column, Integer, DECIMAL, ForeignKey, Identity
from sqlalchemy.orm import relationship
from app.database import Base

class Budget(Base):
    __tablename__ = "budgets"

    budget_id = Column(Integer, Identity(start=1, increment=1), primary_key=True, index=True)
    amount = Column(DECIMAL(10, 2), nullable=False)
    total_spent = Column(DECIMAL(10, 2), default=0)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    # Relationships
    user = relationship("User", back_populates="budget")