
from typing import Optional
from pydantic import BaseModel, ConfigDict
from .department_schema import DepartmentResponse
    
class CategoryInsert(BaseModel):
    category_name: str
    department_id: int
    
class CategoryResponse(BaseModel):
    category_id: int
    category_name: str
    department: Optional[DepartmentResponse] 
    
    model_config = ConfigDict(from_attributes=True)
    
class CategoriesResponse(BaseModel):
    categories: list[CategoryResponse]