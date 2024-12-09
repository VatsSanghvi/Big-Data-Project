from pydantic import BaseModel, ConfigDict
from typing import List, Optional

from app.schemas.product_schema import ProductResponse


class GroceryListBase(BaseModel):
    id: int
    name: str
    total_spent: float
    user_id: int

    model_config = ConfigDict(from_attributes=True)

class GroceryListCreate(BaseModel):
    name: str
    user_id: int

class GroceryItemBase(BaseModel):
    id: int
    quantity: int
    grocery_list_id: int
    product_id: int

    model_config = ConfigDict(from_attributes=True)

class GroceryListResponse(GroceryListBase):
    items: List[GroceryItemBase]

    model_config = ConfigDict(from_attributes=True)

class GroceryItemCreate(BaseModel):
    quantity: int
    grocery_list_id: int
    product_id: int

class GroceryItemResponse(GroceryItemBase):
    product: Optional[ProductResponse]

    model_config = ConfigDict(from_attributes=True)


