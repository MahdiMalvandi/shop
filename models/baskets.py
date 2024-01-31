from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Base
from sqlalchemy.orm import relationship


class Basket(Base):
    __tablename__ = 'baskets'
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer)

    # Foreign Keys
    color_selected = Column(Integer, ForeignKey('colors.id'))
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    # Relationships

    # Product
    products = relationship('models.products.Product', back_populates='baskets')

    # User
    user = relationship('User', back_populates='baskets')

    # Color
    colors = relationship('Color', back_populates='baskets')
