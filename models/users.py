from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Base
from models.products import Product
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    profile = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)
    is_seller = Column(Boolean, default=False)

    # Relationships

    # Product
    products = relationship('Product', back_populates='seller')

    # Basket
    baskets = relationship('Basket', back_populates='user')

    # Comment
    comments = relationship('Comment', back_populates='user')

    # Order
    orders = relationship('Order', back_populates='user')

    # Discount Code
    discount_codes = relationship('DiscountCode', back_populates='user')

    # Category
    category = relationship('Category', back_populates='user')


