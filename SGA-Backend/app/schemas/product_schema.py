
from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import date
from app.schemas.category_schema import CategoryResponse
from app.schemas.department_schema import DepartmentResponse
from app.schemas.store_schema import StoreResponse

class ProductBase(BaseModel):
    product_id: int
    product_name: str
    stock_quantity: int
    price: float
    status: str
    unit_of_measure: str
    ingredients: str
    price_valid_from: date
    price_valid_to: date
    fk_category_id: int
    fk_department_id: Optional[int]
    fk_store_id: Optional[int]
    
class ProductInsert(BaseModel):
    product_name: str
    stock_quantity: int
    price: float
    status: str
    unit_of_measure: str
    ingredients: str
    price_valid_from: date
    price_valid_to: date
    fk_category_id: int
    fk_department_id: Optional[int]
    fk_store_id: Optional[int]
    
class ProductResponse(ProductBase):
    category: Optional[CategoryResponse] 
    department: Optional[DepartmentResponse] 
    store: Optional[StoreResponse] 
    
    model_config = ConfigDict(from_attributes=True)