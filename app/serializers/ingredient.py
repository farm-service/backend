from pydantic.main import BaseModel
from app.serializers.units_of_measurement import UnitOfMeasurementSerializer


class IngredientModel(BaseModel):
    id: int
    name: str
    measure_unit_id: int
    measure_unit: UnitOfMeasurementSerializer
