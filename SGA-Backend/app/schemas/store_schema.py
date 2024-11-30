from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal

# Store schemas
class StoreInsert(BaseModel):
    store_name: str
    location: str
    fk_owner_id: int

class StoreBase(BaseModel):
    store_id: int
    store_name: str
    location: str

class StoreResponse(StoreBase):
    model_config = ConfigDict(from_attributes=True)

# Price comparison schemas
class StorePriceBase(BaseModel):
    price: Decimal
    price_valid_from: datetime
    price_valid_until: datetime
    quantity_limit: Optional[int] = None
    is_on_sale: bool = False

class StorePriceCompare(StorePriceBase):
    store: StoreBase  # Changed from Store to StoreBase

    model_config = ConfigDict(from_attributes=True)

class ProductPriceComparison(BaseModel):
    product_id: int
    product_name: str
    store_prices: List[StorePriceCompare]

    model_config = ConfigDict(from_attributes=True)