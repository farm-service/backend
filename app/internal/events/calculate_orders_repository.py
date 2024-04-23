from abc import ABC
from datetime import datetime
from typing import List, Optional

from app.domain.repositories.calculate_orders_repository_interface import CalculateOrdersRepositoryInterface
from app.models import ProductIngredientAssociation, OrderItem


class CalculateOrdersRepository(CalculateOrdersRepositoryInterface):

    async def get_items_by_product(self, product_id: str) -> Optional[List[ABC]]:
        """
        Method returns items for recipe

        Args:
            product_id (str): id of product for recipe

        Returns:
            Optional[List[ABC]]: List of recipes by product_id or None
        """
        return await ProductIngredientAssociation.get_items_by_product(product_id)

    def construct_order_instances(
            self,
            amount: int,
            deadline: datetime,
            status_id: int,
            ingredient_id: int,
            consumer_id: any,
            producer_id: any
    ) -> Optional[List[ABC]]:
        return OrderItem(
            amount=amount,
            deadline=deadline,
            status_id=status_id,
            ingredient_id=ingredient_id,
            consumer_id=consumer_id,
            producer_id=producer_id
        )

    async def save_orders(self, orders: any):
        await OrderItem.create_or_update_orders(orders)
