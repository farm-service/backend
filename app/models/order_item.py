import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, UUID
from sqlalchemy.orm import relationship

from app.models.base import Base


class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    amount = Column(Integer, nullable=False)
    created = Column(TIMESTAMP, default=datetime.utcnow)
    modified = Column(TIMESTAMP, default=datetime.utcnow())
    date_deliver = Column(TIMESTAMP, default=datetime.utcnow(), nullable=True)
    deadline = Column(TIMESTAMP, default=datetime.utcnow())
    status = Column(Integer, ForeignKey('order_status.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    consumer_id = Column(UUID, ForeignKey('user.id'))
    producer_id = Column(UUID, ForeignKey('user.id'), nullable=True)
    consumer = relationship('User', foreign_keys=[consumer_id])
    producer = relationship('User', foreign_keys=[producer_id])
    ingredient = relationship('Ingredient')

    def __str__(self):
        return f"{self.id}_{self.name}"
