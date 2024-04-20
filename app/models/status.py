from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Status(Base):
    __tablename__ = 'order_status'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __str__(self):
        return f"{self.id}_{self.name}"
