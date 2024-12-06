from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from app.schemas.user_schema import UserResponse

class StoreCreateRequest(BaseModel):
    store_name: str
    location: str
    fk_owner_id: int
    manager_email: Optional[str] = None

class StoreUpdateRequest(BaseModel):
    store_name: str
    location: str
    manager_email: Optional[str] = None

class StoreBase(BaseModel):
    store_id: int
    store_name: str
    location: str

class StoreResponse(StoreBase):
    manager: Optional[UserResponse]
    model_config = ConfigDict(from_attributes=True)

# Price comparison schemas
class StorePriceBase(BaseModel):
    price: Decimal
    quantity_limit: Optional[int] = None
    is_on_sale: bool = False

class StorePriceCompare(StorePriceBase):
    store: StoreBase

    model_config = ConfigDict(from_attributes=True)

class PriceComparisonRequest(BaseModel):
    product_id: int
    product_name: str
    store_prices: List[StorePriceCompare]

    model_config = ConfigDict(from_attributes=True)

class FlyerResponse(BaseModel):
    flyer_id: int
    store_id: int
    flyer_url: str

    model_config = ConfigDict(from_attributes=True)