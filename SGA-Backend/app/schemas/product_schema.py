
from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import date
from enum import Enum
from app.schemas.category_schema import CategoryResponse
from app.schemas.department_schema import DepartmentResponse
from app.schemas.store_schema import StoreResponse

class ProductStatus(str, Enum):
    IN_STOCK = "In Stock",
    OUT_OF_STOCK = "Out of Stock"
    
class ProductInsert(BaseModel):
    product_name: str
    price: float
    status: ProductStatus
    ingredients: str
    price_valid_from: date
    price_valid_to: date
    category_id: int
    department_id: int
    store_id: int
    
class ProductResponse(BaseModel):
    id: int
    product_name: str
    price: float
    status: ProductStatus
    ingredients: str
    price_valid_from: date
    price_valid_to: date
    category: Optional[CategoryResponse] 
    department: Optional[DepartmentResponse] 
    store: Optional[StoreResponse] 
    
    model_config = ConfigDict(from_attributes=True)
    
class ProductsResponse(BaseModel):
    products: List[ProductResponse]