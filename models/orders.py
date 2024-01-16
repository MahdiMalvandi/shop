from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Model
from sqlalchemy.orm import relationship


class Orders(Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer)

    # Foreign Keys
    color_selected = Column(Integer, ForeignKey('colors'))
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    discount_code_id = Column(Integer, ForeignKey("discount_codes.id"), nullable=True)

    # Relationships

    # Product
    products = relationship('Product', back_populates='order')

    # User
    user = relationship('User', back_populates='order')

    # Color
    color = relationship('Color', back_populates='order')

    # Discount Code
    discount_code = relationship('DiscountCode', back_populates='order', nullable=True)
