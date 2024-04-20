from sqladmin import ModelView
from app.models.status import Status


class StatusAdmin(ModelView, model=Status):
    column_list = [
        Status.id,
        Status.name
    ]
    category = "directory"
    name_plural = 'Statuses'
