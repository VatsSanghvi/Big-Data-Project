from pydantic import BaseModel, ConfigDict
    
class CategoryInsert(BaseModel):
    category_name: str
    fk_department_id: int
    
class CategoryResponse(BaseModel):
    category_id: int
    category_name: str
    fk_department_id: int

    model_config = ConfigDict(from_attributes=True)
    
class CategoriesResponse(BaseModel):
    categories: list[CategoryResponse]