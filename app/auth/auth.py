from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, CookieTransport
from app.configuration.settings import SECRET_JWT
from fastapi_users import FastAPIUsers
from app.auth.models import User
from app.auth.manager import get_user_manager
import uuid

cookie_transport = CookieTransport(
    cookie_max_age=3600,
    cookie_samesite="none",
    cookie_name="token",
    cookie_secure=False,
    cookie_httponly=False
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=SECRET_JWT,
        lifetime_seconds=3600,
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
