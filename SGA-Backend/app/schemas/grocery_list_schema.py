from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class GroceryListBase(BaseModel):
    name: str
    user_id: int

class GroceryItemBase(BaseModel):
    name: str
    category: str
    grocery_list_id: int

class GroceryListCreate(GroceryListBase):
    pass

class GroceryItemCreate(GroceryItemBase):
    pass

class GroceryItemResponse(GroceryItemBase):
    model_config = ConfigDict(from_attributes=True)

class GroceryItem(GroceryItemBase):
    id: int
    name: str
    category: str

    model_config = ConfigDict(from_attributes=True)

class GroceryListResponse(GroceryListBase):
    items: Optional[List[GroceryItem]]

    model_config = ConfigDict(from_attributes=True)

