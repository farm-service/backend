from abc import ABC
from datetime import datetime
from typing import List, Optional


class CalculateOrdersRepositoryInterface(ABC):

    async def get_items_by_product(self, product_id: str) -> Optional[List[ABC]]:
        """
        Method returns items for recipe

        Args:
            product_id (str): id of product for recipe

        Returns:
            Optional[List[BaseModel]]: List of recipes by product_id or None
        """
        raise Exception('Method get_items_by_product must be implemented')

    def construct_order_instances(
            self,
            amount: int,
            deadline: datetime,
            status_id: int,
            ingredient_id: int,
            consumer_id: any,
            producer_id: any
    ) -> Optional[List[ABC]]:
        raise Exception('Method construct_order_instances must be implemented')

    async def save_orders(self, orders: list):
        raise Exception('Method save_orders must be implemented')
