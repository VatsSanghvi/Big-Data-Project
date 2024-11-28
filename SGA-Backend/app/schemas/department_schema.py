
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.store_schema import StoreResponse

class DepartmentBase(BaseModel):
    department_id: int
    department_name: str
    
class DepartmentCreate(BaseModel):
    department_name: str
    fk_store_id: int
    
class DepartmentResponse(DepartmentBase):
    store: Optional[StoreResponse] 
    
    model_config = ConfigDict(from_attributes=True)