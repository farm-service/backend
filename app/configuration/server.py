from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from apscheduler.schedulers.background import BackgroundScheduler
import uuid

from fastapi_users import FastAPIUsers
from sqladmin import Admin

from app.admin.auth import AdminAuth
from app.configuration.routes import __routes__
from app.configuration.admin import __admins__
from app.auth.auth import auth_backend
from app.configuration.settings import SECRET_JWT
from app.internal.events.generate_orders import generate_orders
from app.models.user import User
from app.auth.schemas import UserRead, UserCreate
from app.auth.manager import get_user_manager
from app.auth import engine


class Server:
    app: FastAPI

    def __init__(self, app: FastAPI):
        self.__app = app
        self.__engine = engine
        self.__register_routes(app)
        self.__register_events(app)
        self.__register_admin(app)

    def get_app(self) -> FastAPI:
        return self.__app

    @staticmethod
    def __register_events(app: FastAPI) -> None:
        app.on_event('startup')(repeat_every(seconds=60 * 60 * 12)(generate_orders))
        # configure scheduler
        scheduler = BackgroundScheduler()
        scheduler.add_job(generate_orders, "cron", hour=0, day_of_week='sun')
        scheduler.start()

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

    @staticmethod
    def __register_admin(app: FastAPI) -> None:
        authentication_backend = AdminAuth(secret_key=SECRET_JWT)
        admin = Admin(
            app,
            engine,
            authentication_backend=authentication_backend
        )
        __admins__.register_admins(admin)
