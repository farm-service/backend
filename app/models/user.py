from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, UUID
from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from datetime import datetime
import uuid

from app.models.base import Base
from app.models.role import Role


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'user'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey('role.id'))
    role = relationship('Role')
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
