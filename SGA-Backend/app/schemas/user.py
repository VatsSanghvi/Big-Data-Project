from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    CUSTOMER = "customer"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: Optional[str] = None
    address: Optional[str] = None
    role: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str
    
class UserResponseTest(BaseModel):
    ok: bool
    token: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: Optional[str] = None
    address: Optional[str] = None
    role: UserRole

    class Config:
        from_attributes = True

