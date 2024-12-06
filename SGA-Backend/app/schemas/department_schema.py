from pydantic import BaseModel, ConfigDict

class DepartmentBase(BaseModel):
    department_id: int
    department_name: str
    
class DepartmentCreate(BaseModel):
    department_name: str
    fk_store_id: int
    
class DepartmentResponse(DepartmentBase):
    model_config = ConfigDict(from_attributes=True)