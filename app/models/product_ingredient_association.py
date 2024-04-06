from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

from app.models import Product, Ingredient


class ProductIngredientAssociation(Base):
    __tablename__ = 'product_ingredient_association'

    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    nominal_coefficient = Column(Float)

    product = relationship("Product", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="product")
