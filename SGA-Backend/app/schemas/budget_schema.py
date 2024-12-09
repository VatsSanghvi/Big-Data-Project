from pydantic import BaseModel, ConfigDict
from decimal import Decimal

class BudgetBase(BaseModel):
    budget_id: int
    amount: Decimal
    user_id: int
    total_spent: Decimal = Decimal(0)

class BudgetCreate(BaseModel):
    amount: Decimal

class BudgetResponse(BudgetBase):
    model_config = ConfigDict(from_attributes=True)

class BudgetUpdate(BaseModel):
    amount: Decimal