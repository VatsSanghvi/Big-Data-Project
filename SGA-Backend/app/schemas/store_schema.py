
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.user_schema import UserResponse
    
class StoreInsert(BaseModel):
    store_name: str
    location: str
    fk_manager_id: int
    
class StoreResponse(BaseModel):
    store_id: int
    store_name: str
    location: str
    manager: Optional[UserResponse]
    
    model_config = ConfigDict(from_attributes=True)
    
class StoresResponse(BaseModel):
    stores: list[StoreResponse]