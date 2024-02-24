from sqlalchemy.orm import DeclarativeBase
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from datetime import datetime
from app.models.models import role


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    role_id = Column(Integer, ForeignKey(role.c.id))
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
