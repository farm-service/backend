from uuid import UUID

from pydantic.main import BaseModel


class ProductSerializer(BaseModel):
    id: int
    name: str
    owner_id: UUID
