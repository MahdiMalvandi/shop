from typing import Optional

from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class Register(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    profile: Optional[str] = None
    password: str
