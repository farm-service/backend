from sqlalchemy.orm import DeclarativeBase, relationship
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, JSON
from datetime import datetime
from app.models.models import role


class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship("Role")
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
