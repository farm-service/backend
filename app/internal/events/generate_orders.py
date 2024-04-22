from typing import NoReturn

from app.configuration.settings import logger
from app.domain.calculate_orders import CalculateOrders
from app.internal.integrations.get_forecast import GetForecast
from app.models import ProductIngredientAssociation, OrderItem


async def generate_orders() -> NoReturn:
    """
    Event generate orders from forecast
    Returns: NoReturn

    """
    try:
        forecast = await GetForecast.get_forecast()
        calculated_orders = await CalculateOrders.process(
            forecast=forecast,
            recipe_model=ProductIngredientAssociation,
            order_model=OrderItem
        )
        await OrderItem.create_or_update_orders(calculated_orders)
    except Exception as e:
        logger.error(f'Exception occurred: {e}')
