from fastapi import APIRouter

from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()

# region Authentication
pwd_cxt = CryptContext(schemes=)
# endregion
