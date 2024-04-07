import uuid
from passlib.context import CryptContext

from fastapi_users.jwt import generate_jwt
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from app.auth import async_session_maker
from app.auth.manager import UserManager
from app.models import User
from app.serializers.user import UserSerializer


class AdminAuth(AuthenticationBackend):

    def __init__(self, secret_key):
        super().__init__(secret_key)
        self.secret_key = secret_key

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]
        async with async_session_maker() as session:
            user_db = SQLAlchemyUserDatabase(session, User)
            user_manager = UserManager(user_db)
            user = await user_manager.get_by_email(user_email=username)
            pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
            checked_password = pwd_context.verify(password, user.hashed_password)

            if user is None or not checked_password:
                return False

            user_data = UserSerializer(
                id=str(user.id),
                email=user.email,
                username=user.username,
                registered_at=str(user.registered_at),
                role_id=user.role_id,
                hashed_password=user.hashed_password,
                is_active=user.is_active,
                is_superuser=user.is_superuser,
                is_verified=user.is_verified
            )

            token = generate_jwt(user_data.dict(), lifetime_seconds=None, secret=self.secret_key)
            request.session.update({"token": token})

            return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        return True
