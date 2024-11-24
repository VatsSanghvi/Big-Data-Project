from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.department_schema import DepartmentResponse
    
class CategoryInsert(BaseModel):
    category_name: str
    fk_department_id: int
    
class CategoryResponse(BaseModel):
    category_id: int
    category_name: str
    fk_department_id: int
    #department: Optional[DepartmentResponse]

    model_config = ConfigDict(from_attributes=True)
    
class CategoriesResponse(BaseModel):
    categories: list[CategoryResponse]