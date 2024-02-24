from sqlalchemy.orm import DeclarativeBase, relationship
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from sqlalchemy import JSON, Column, ForeignKey, Integer, String, TIMESTAMP, Enum
from enum import Enum as PyEnum
from datetime import datetime


class Base(DeclarativeBase):
    pass


class RoleEnum(PyEnum):
    PRODUCER = "producer"
    CONSUMER = "consumer"


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(RoleEnum), unique=True)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
