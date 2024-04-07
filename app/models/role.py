from sqlalchemy import Column, Integer, String, JSON

from app.models.base import Base


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

    def __str__(self):
        return f'{self.name}'
