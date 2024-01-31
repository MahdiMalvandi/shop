from typing import Optional
from pydantic import BaseModel
from .users import User
from .products import Product, ProductColor


class BasketBase(BaseModel):
    count: int


class Basket(BasketBase):
    id: int
    color_selected: ProductColor
    product: Product
    user: User


class BasketCreate(BasketBase):
    color_selected: str
    product: str
    user: str
