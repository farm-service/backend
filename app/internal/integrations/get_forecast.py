import aiohttp

from app.configuration.settings import URL_FORCAST


class GetForecast:
    """
    Integration class with farm-ML service
    """

    @classmethod
    async def get_forcast(cls):
        """
        Get forecast from farm-ML service
        Returns (Dict): Forecast dictionary

        """
        async with aiohttp.ClientSession() as session:
            async with session.get(URL_FORCAST) as response:
                return await response.json()
