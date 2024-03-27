from pydantic import BaseModel, EmailStr, Field
from typing import Optional



class UserBase(BaseModel):
    name: str = Field(..., alias="Name")
    surname: str
    email: Optional[EmailStr] = None

    class Config:
        allow_population_by_field_name = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

 
class UserInDB(UserInDBBase):
    hash_password: str


class User(UserInDBBase):
    pass