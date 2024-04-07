from sqladmin import ModelView
from app.models.units_of_measurement import UnitOfMeasurement


class UnitOfMeasurementAdmin(ModelView, model=UnitOfMeasurement):
    column_list = [
        UnitOfMeasurement.id,
        UnitOfMeasurement.name,
        UnitOfMeasurement.abbreviation
    ]

    category = "directory"
