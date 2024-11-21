
from typing import Optional
from pydantic import BaseModel, ConfigDict
from .store_schema import StoreResponse
    
class DepartmentCreate(BaseModel):
    department_name: str
    store_id: int
    
class DepartmentResponse(BaseModel):
    department_name: str
    store: Optional[StoreResponse] 
    
    model_config = ConfigDict(from_attributes=True)
    
class DepartmentsResponse(BaseModel):
    departments: list[DepartmentCreate]