from pydantic import BaseModel

class CategoryBase(BaseModel):
    title: str
    description: str


class Category(CategoryBase):
    id: int




