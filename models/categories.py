from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Model
from sqlalchemy.orm import relationship


class Category(Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

    # Relationships

    # Product
    products = relationship('Product', back_populates='basket')

    # User
    user = relationship('User', back_populates='basket')

    # Color
    color = relationship('Color', back_populates='basket')
