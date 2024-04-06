import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, Boolean, String, UUID
from sqlalchemy.orm import relationship

from app.models.base import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created = Column(TIMESTAMP, default=datetime.utcnow)
    owner_id = Column(UUID, ForeignKey('user.id'))
    owner = relationship('User')
    is_active = Column(Boolean, default=True, nullable=False)
    ingredients = relationship("ProductIngredientAssociation", back_populates="product")
