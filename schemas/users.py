from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    profile: Optional[str] = None
    is_admin: bool = False
    is_seller: bool = False


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
