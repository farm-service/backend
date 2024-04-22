from datetime import datetime, timedelta

import pytz
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import List, Optional, Dict, Type

from app.configuration.settings import logger


class CalculateOrders:
    """
    This class responsible for calculating orders based on an existing forecast
    """

    @classmethod
    async def process(
            cls,
            forecast: Optional[Dict[str, dict]],
            recipe_model: Type[DeclarativeMeta],
            order_model: Type[DeclarativeMeta]
    ) -> List[DeclarativeMeta]:
        """
        Processes the forecast data to generate orders

        Args:
            forecast (Optional[Dict[str, dict]]): A dictionary containing forecast data
            recipe_model (Type[DeclarativeMeta]): The model class representing recipe data
            order_model (Type[DeclarativeMeta]): The model class representing order data

        Returns:
            List[DeclarativeMeta]: A list of order objects generated based on the forecast data
        """
        result = list()
        try:
            for product_id, value in forecast.items():
                recipe = await recipe_model.get_items_by_product(product_id)
                for date, amount in value.items():
                    # TODO: working with timezone is temp design. Delete when ML-service return right datetime objects
                    dt_without_timezone = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                    timezone = pytz.timezone('Europe/Moscow')
                    dt_with_timezone = timezone.localize(dt_without_timezone) - timedelta(days=1)
                    for ingredient in recipe:
                        result.append(
                            order_model(
                                amount=amount * ingredient.nominal_coefficient,
                                deadline=dt_with_timezone,
                                status_id=1,
                                ingredient_id=ingredient.ingredient.id if ingredient.ingredient is not None else None,
                                consumer_id=ingredient.product.owner_id if ingredient.product is not None else None,
                                producer_id=None
                            )
                        )
            return result
        except Exception as e:
            logger.error(f'Exception occurred: {e}')
