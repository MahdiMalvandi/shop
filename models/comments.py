from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Model
from sqlalchemy.orm import relationship


class Comment(Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    body = Column(String, nullable=False)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    # Relationships

    # Product
    products = relationship('Product', back_populates='comments')

    # User
    user = relationship('User', back_populates='comments')
