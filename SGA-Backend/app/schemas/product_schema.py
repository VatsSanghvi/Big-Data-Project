
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.category_schema import CategoryResponse
from app.schemas.department_schema import DepartmentResponse
from app.schemas.store_schema import StoreResponse

class ProductBase(BaseModel):
    product_id: int
    product_name: str
    stock_quantity: int
    price: float
    status: str
    
class ProductCreateRequest(BaseModel):
    product_name: str
    stock_quantity: int
    price: float
    fk_category_id: int
    fk_department_id: int
    fk_store_id: int
    
class ProductResponse(ProductBase):
    category: Optional[CategoryResponse] 
    department: Optional[DepartmentResponse] 
    store: Optional[StoreResponse] 
    
    model_config = ConfigDict(from_attributes=True)