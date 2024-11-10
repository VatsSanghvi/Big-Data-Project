from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: Optional[str] = None
    address: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role: str  

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class UserResponse(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True
