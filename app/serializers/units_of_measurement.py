from pydantic.main import BaseModel


class UnitOfMeasurementSerializer(BaseModel):
    id: int
    name: str
    abbreviation: str
