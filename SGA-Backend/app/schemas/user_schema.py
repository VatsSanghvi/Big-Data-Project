from pydantic import BaseModel, EmailStr, ConfigDict, constr
from typing import List, Optional

class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: Optional[str] = None
    role: str

class UserUpdate(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    phone_number: str

class UserBase(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None
    role: str

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

class UsersResponse(BaseModel):
    ok: bool
    msg: str
    users: List[UserResponse]

class PasswordReset(BaseModel):
    sender_email: EmailStr
    to_email: EmailStr

class PasswordUpdate(BaseModel):
    user_id: int
    current_password: str
    new_password: constr(min_length=8)



    
