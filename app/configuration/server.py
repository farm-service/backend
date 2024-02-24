from fastapi import FastAPI
from app.configuration.routes import __routes__


class Server:
    app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__register_routes(app)
        self.__register_events(app)

    def get_app(self) -> FastAPI:
        return self.__app

    @staticmethod
    def __register_events(app: FastAPI) -> None:
        ...

    @staticmethod
    def __register_routes(app: FastAPI) -> None:
        __routes__.register_routes(app)
