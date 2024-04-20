import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, UUID
from sqlalchemy.orm import relationship

from app.models.base import Base


class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    amount = Column(Integer, nullable=False)
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    modified = Column(TIMESTAMP(timezone=True), default=datetime.utcnow())
    date_deliver = Column(TIMESTAMP(timezone=True), default=datetime.utcnow(), nullable=True)
    deadline = Column(TIMESTAMP(timezone=True), default=datetime.utcnow())
    status = Column(Integer, ForeignKey('order_status.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    consumer_id = Column(UUID, ForeignKey('user.id'))
    producer_id = Column(UUID, ForeignKey('user.id'), nullable=True)
    consumer = relationship('User', foreign_keys=[consumer_id])
    producer = relationship('User', foreign_keys=[producer_id])
    ingredient = relationship('Ingredient')

    def __str__(self):
        consumer_name = self.consumer.name if self.consumer else "Unknown"
        ingredient_name = self.ingredient.name if self.ingredient.name else "Unknown"
        return f"{consumer_name}_{ingredient_name}_{self.amount}"
