from sqlalchemy import Integer, Column, Boolean, String, ForeignKey
from settings.database import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationships

    # Product
    products = relationship('Product', back_populates='category')

    # User
    user = relationship('User', back_populates='category')


