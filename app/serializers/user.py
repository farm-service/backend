from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserSerializer(BaseModel):
    id: Optional[str]
    email: str
    username: str
    registered_at: Optional[str]
    role_id: Optional[int]
    hashed_password: str
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]

    class Config:
        orm_mode = True
