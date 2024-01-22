from pydantic import BaseModel
from products import Product


class CategoryBase(BaseModel):
    title: str
    description: str


class Category(CategoryBase):
    id: int


class CategoryWithPosts(CategoryBase):
    products: list[Product]

