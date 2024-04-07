from sqladmin import ModelView
from app.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.username,
        User.email,
        User.role,
        User.is_superuser
    ]
    category = "users"
