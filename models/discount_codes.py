from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Base
from sqlalchemy.orm import relationship
from .orders import Order



class DiscountCode(Base):
    __tablename__ = 'discount_codes'

    id = Column(Integer, primary_key=True)
    percent = Column(Integer)
    code = Column(String, unique=True)

    # Foreign Keys

    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    # Relationships

    # Product
    products = relationship('Product', back_populates='discount_codes')

    # User
    user = relationship('User', back_populates='discount_codes')

    # Order
    orders = relationship('Order', back_populates='discount_codes')
