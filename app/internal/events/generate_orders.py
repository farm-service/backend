from app.domain.calculate_orders import CalculateOrders
from app.internal.integrations.get_forecast import GetForecast
from app.models import ProductIngredientAssociation, OrderItem


async def generate_orders():
    """
    Event generate orders from forecast
    Returns:

    """
    forecast = await GetForecast.get_forecast()
    calculated_orders = await CalculateOrders.process(
        forecast=forecast,
        recipe_model=ProductIngredientAssociation,
        order_model=OrderItem
    )
    await OrderItem.create_or_update_orders(calculated_orders)
