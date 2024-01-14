from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Model
from sqlalchemy.orm import relationship


class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    profile = Column(String, nullable=True)
    is_admin = Column(Boolean)
    is_seller = Column(Boolean)

    # Relationships

    # Product
    products = relationship('Product', back_populates='seller')

    # Basket
    basket = relationship('Basket', back_populates='user')

    # Comment
    comments = relationship('Comment', back_populates='user')

    # Order
    basket = relationship('Order', back_populates='user')

    # Basket
    basket = relationship('Basket', back_populates='user')


