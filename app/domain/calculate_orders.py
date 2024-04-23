from datetime import datetime, timedelta

import pytz
from typing import Optional, Dict

from app.domain.repositories.calculate_orders_repository_interface import CalculateOrdersRepositoryInterface


class CalculateOrders:
    """
    This class responsible for calculating orders based on an existing forecast
    """

    @classmethod
    async def process(
            cls,
            forecast: Optional[Dict[str, dict]],
            repository: CalculateOrdersRepositoryInterface
    ) -> None:
        """
        Processes the forecast data to generate orders

        Args:
            forecast (Optional[Dict[str, dict]]): A dictionary containing forecast data
            repository (CalculateOrdersRepositoryInterface): The repository that implements access to data layer

        Returns:
            None
        """
        result = list()
        for product_id, value in forecast.items():
            recipe = await repository.get_items_by_product(product_id)
            for date, amount in value.items():
                # TODO: working with timezone is temp design. Delete when ML-service return right datetime objects
                dt_without_timezone = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                timezone = pytz.timezone('Europe/Moscow')
                # annotate deadline
                dt_with_timezone = timezone.localize(dt_without_timezone) - timedelta(days=1)
                for ingredient in recipe:
                    result.append(
                        repository.construct_order_instances(
                            amount=amount * ingredient.nominal_coefficient,
                            deadline=dt_with_timezone,
                            status_id=1,
                            ingredient_id=ingredient.ingredient.id if ingredient.ingredient is not None else None,
                            consumer_id=ingredient.product.owner_id if ingredient.product is not None else None,
                            producer_id=None
                        )
                    )
        await repository.save_orders(orders=result)
