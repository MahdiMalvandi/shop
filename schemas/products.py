from typing import Optional

from pydantic import BaseModel
from .categories import Category
from .users import User


class ProductBase(BaseModel):
    title: str
    price: float
    discount: float
    count: int


class ProductImage(BaseModel):
    title: str
    photo: str


class ProductAttribute(BaseModel):
    key: str
    value: str


class ProductColor(BaseModel):
    color: str


class Product(ProductBase):
    id: int
    category: Category
    seller: User
    product_colors: list[ProductColor]
    product_attributes: list[ProductAttribute]
    product_images: list[ProductImage]
    slug: str


class ProductCreate(ProductBase):
    category_id: id
    product_colors: Optional[str | list]
    product_attributes: Optional[str | list]
    product_images: Optional[str | list]


class CategoryWithPosts(Category):
    products: list[Product]


class UserWithProducts(User):
    products: list[Product]
