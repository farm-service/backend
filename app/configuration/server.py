from fastapi import FastAPI
import uuid

from fastapi_users import FastAPIUsers
from app.configuration.routes import __routes__
from app.auth.auth import auth_backend
from app.auth.models import User
from app.auth.schemas import UserRead, UserCreate
from app.auth.manager import get_user_manager


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
        fastapi_users = FastAPIUsers[User, uuid.UUID](
            get_user_manager,
            [auth_backend],
        )
        app.include_router(
            fastapi_users.get_auth_router(auth_backend),
            prefix="/auth/jwt",
            tags=["auth"],
        )
        app.include_router(
            fastapi_users.get_register_router(UserRead, UserCreate),
            prefix="/auth",
            tags=["auth"],
        )
        __routes__.register_routes(app)
