from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Base
from sqlalchemy.orm import relationship

from models.comments import Comment
from .discount_codes import DiscountCode
from .categories import Category
from models import baskets, orders


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Integer)
    discount = Column(Integer)
    slug = Column(String)
    count = Column(Integer)

    # Foreign keys
    category_id = Column(Integer, ForeignKey('categories.id'))
    seller_id = Column(Integer, ForeignKey('users.id'))

    # Relationships

    # User
    seller = relationship("User", back_populates='products')

    # Color
    colors = relationship("ProductColor", back_populates='products')

    # Comment
    comments = relationship("Comment", back_populates='products')

    # Image
    images = relationship("ProductImage", back_populates='products')

    # Attribute
    attributes = relationship("ProductAttribute", back_populates='products')

    # Discount Code
    discount_codes = relationship("DiscountCode", back_populates='products')

    # Category
    category = relationship("models.categories.Category", back_populates='products')

    # Basket
    baskets = relationship("models.baskets.Basket", back_populates='products')

    # Order
    orders = relationship("Order", back_populates='products')


class ProductImage(Base):
    __tablename__ = 'product_images'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    photo = Column(String)

    # Foreign Keys
    product_id = Column(Integer, ForeignKey('products.id'))

    # Relationships

    # Product
    products = relationship("Product", back_populates='images')


class ProductAttribute(Base):
    __tablename__ = 'product_attributes'
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String)
    value = Column(String)

    # Foreign Keys
    product_id = Column(Integer, ForeignKey('products.id'))

    # Relationships

    # Product
    products = relationship("Product", back_populates='attributes')


class ProductColor(Base):
    __tablename__ = 'product_colors'
    id = Column(Integer, primary_key=True, index=True)

    # Foreign Keys
    product_slug = Column(String, ForeignKey('products.slug'))
    color_id = Column(Integer, ForeignKey('colors.id'))

    # Relationships

    # Product
    products = relationship("Product", back_populates='colors')

    # Through
    colors = relationship("Color", back_populates='through')


class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, index=True)
    color = Column(String)

    # Relationships

    # Through
    through = relationship("ProductColor", back_populates='colors')

    baskets = relationship('Basket', back_populates='colors')

    orders = relationship("models.orders.Order", back_populates='colors')
