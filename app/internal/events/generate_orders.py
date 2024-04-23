from typing import NoReturn

from app.configuration.settings import logger
from app.domain.calculate_orders import CalculateOrders
from app.internal.events.calculate_orders_repository import CalculateOrdersRepository
from app.internal.integrations.get_forecast import GetForecast


async def generate_orders() -> NoReturn:
    """
    Event generate orders from forecast
    Returns: NoReturn

    """
    try:
        forecast = await GetForecast.get_forecast()
        await CalculateOrders.process(
            forecast=forecast,
            repository=CalculateOrdersRepository()
        )
    except Exception as e:
        logger.error(f'Exception occurred: {e}')
