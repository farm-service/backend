from sqlalchemy import Column, Integer, String

from app.models.base import Base


class UnitOfMeasurement(Base):
    __tablename__ = 'units_of_measurement'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    abbreviation = Column(String, unique=True)
