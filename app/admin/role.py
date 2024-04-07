from sqladmin import ModelView
from app.models.role import Role


class RoleAdmin(ModelView, model=Role):
    column_list = [
        Role.id,
        Role.name,
        Role.permissions
    ]
    category = "users"

