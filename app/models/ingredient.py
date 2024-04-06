from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measure_unit_id = Column(Integer, ForeignKey('units_of_measurement.id'))
    measure_unit = relationship("UnitOfMeasurement")
    product = relationship("ProductIngredientAssociation", back_populates="ingredient")
