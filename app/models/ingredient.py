from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.units_of_measurement import UnitOfMeasurement


class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    measure_unit_id = Column(Integer, ForeignKey('units_of_measurement.id'))
    measure_unit = relationship("UnitOfMeasurement")

# TODO: Создать справочник для хранинеия категорий ингредиентов
