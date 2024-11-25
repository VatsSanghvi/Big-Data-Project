
from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import date
from app.schemas.category_schema import CategoryResponse
from app.schemas.department_schema import DepartmentResponse
from app.schemas.store_schema import StoreResponse
    
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
    fk_department_id: int
    fk_store_id: int
    
class ProductResponse(BaseModel):
    product_id: int
    product_name: str
    stock_quantity: int
    price: float
    status: str
    unit_of_measure: str
    ingredients: str
    price_valid_from: date
    price_valid_to: date
    category: Optional[CategoryResponse] 
    department: Optional[DepartmentResponse] 
    store: Optional[StoreResponse] 
    
    model_config = ConfigDict(from_attributes=True)
    
class ProductsResponse(BaseModel):
    products: List[ProductResponse]