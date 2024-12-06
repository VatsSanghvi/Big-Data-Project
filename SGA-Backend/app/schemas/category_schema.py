from pydantic import BaseModel, ConfigDict

class CategoryBase(BaseModel):
    category_id: int
    category_name: str
    
class CategoryInsert(BaseModel):
    category_name: str
    fk_department_id: int
    
class CategoryResponse(CategoryBase):
    model_config = ConfigDict(from_attributes=True)
