import uuid
from typing import Optional, Union
from passlib.context import CryptContext
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, schemas, models

from app.models.user import User
from app.auth import get_user_db
from app.configuration.settings import SECRET_VERIFICATION


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET_VERIFICATION
    verification_token_secret = SECRET_VERIFICATION

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
