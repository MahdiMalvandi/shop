from pydantic import BaseModel
from .users import User
from .products import Product


class CommentBase(BaseModel):
    body: str


class Comment(CommentBase):
    id: int
    user: User
    product: Product


class CommentCreate(CommentBase):
    user: str
    product: str
