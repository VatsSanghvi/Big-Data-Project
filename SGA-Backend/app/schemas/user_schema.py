from enum import Enum
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List, Optional

class UserLogin(BaseModel):
    email: str
    password: str

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    CUSTOMER = "customer"

class UserRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    role: UserRole

class UserResponse(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    role: UserRole

    model_config = ConfigDict(from_attributes=True)

class UsersResponse(BaseModel):
    ok: bool
    msg: str
    users: List[UserResponse]



    
