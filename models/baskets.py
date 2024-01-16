from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Model
from sqlalchemy.orm import relationship


class Baskets(Model):
    __tablename__ = 'baskets'
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer)

    # Foreign Keys
    color_selected = Column(Integer, ForeignKey('colors'))
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    # Relationships

    # Product
    products = relationship('Product', back_populates='basket')

    # User
    user = relationship('User', back_populates='basket')

    # Color
    color = relationship('Color', back_populates='basket')
