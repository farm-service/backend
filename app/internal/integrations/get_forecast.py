import aiohttp

from app.configuration.settings import URL_FORECAST


class GetForecast:
    """
    Integration class with farm-ML service
    """

    @classmethod
    async def get_forecast(cls):
        """
        Get forecast from farm-ML service
        Returns (Dict): Forecast dictionary

        """
        async with aiohttp.ClientSession() as session:
            async with session.get(URL_FORECAST) as response:
                return await response.json()
