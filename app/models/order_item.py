import traceback
import uuid
from datetime import datetime
from typing import List, NoReturn, Optional

from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, UUID, select, Result
from sqlalchemy.orm import relationship

from app.auth import get_async_session
from app.models.base import Base


class OrderItem(Base):
    __tablename__ = 'order_item'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    amount = Column(Integer, nullable=False)
    created = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    modified = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    date_deliver = Column(TIMESTAMP(timezone=True), default=None, nullable=True)
    deadline = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    status_id = Column(Integer, ForeignKey('order_status.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    consumer_id = Column(UUID, ForeignKey('user.id'))
    producer_id = Column(UUID, ForeignKey('user.id'), nullable=True)
    consumer = relationship('User', foreign_keys=[consumer_id])
    producer = relationship('User', foreign_keys=[producer_id])
    ingredient = relationship('Ingredient')
    status = relationship('Status')

    def __str__(self):
        consumer_name = self.consumer.name if self.consumer else "Unknown"
        ingredient_name = self.ingredient.name if self.ingredient else "Unknown"
        return f"{consumer_name}_{ingredient_name}_{self.amount}"

    @classmethod
    async def create_or_update_orders(cls, orders_data: List['OrderItem']) -> NoReturn:
        try:
            async for session in get_async_session():
                for order_data in orders_data:
                    existing_order: Result = await session.execute(
                        select(OrderItem).filter(
                            cls.deadline == order_data.deadline,
                            cls.ingredient_id == order_data.ingredient_id,
                            cls.consumer_id == order_data.consumer_id
                        ).limit(1)
                    )

                    existing_order: Optional[OrderItem] = existing_order.scalar()
                    if existing_order:
                        existing_order.amount = order_data.amount
                        existing_order.modified = datetime.utcnow()
                        existing_order.date_deliver = order_data.date_deliver
                        existing_order.status_id = order_data.status_id
                        existing_order.producer_id = order_data.producer_id
                        session.add(existing_order)
                    else:
                        session.add(order_data)

                await session.commit()
        except Exception as e:
            traceback.print_exc()
            print(f'Error during commit: {e}')

    @staticmethod
    async def save_order_item(order_item: 'OrderItem') -> None:
        """
        Create or update an OrderItem in the database
        Args:
            order_item (OrderItem): An instance of OrderItem to be saved or updated

        Returns: None

        Example:
        Usage example:
            await OrderItem.save_order_item(order_item_instance, session)
        """
        async for session in get_async_session():
            try:
                session.add(order_item)
                await session.commit()
            except Exception as e:
                print(f'Error during commit: {e}')
