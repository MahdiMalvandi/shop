from typing import Optional

from pydantic import BaseModel
from products import Product, ProductColor
from users import User


class OrderBase(BaseModel):
    count: int


class Order(OrderBase):
    product: Product
    user: User
    discount_count: Optional[str]
    color_selected: ProductColor


class OrderCreate(OrderBase):
    product: str
    user: str
    discount_count: Optional[str]
    color_selected: str