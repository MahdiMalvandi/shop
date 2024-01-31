from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Base
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer)

    # Foreign Keys
    color_selected = Column(Integer, ForeignKey('colors.id'))
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    discount_code_id = Column(Integer, ForeignKey("discount_codes.id"), nullable=True)

    # Relationships

    # Product
    products = relationship('Product', back_populates='orders')

    # User
    user = relationship('User', back_populates='orders')

    # Color
    colors = relationship('Color', back_populates='orders')

    # Discount Code
    discount_codes = relationship('DiscountCode', back_populates='orders')



