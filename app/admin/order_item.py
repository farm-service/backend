from sqladmin import ModelView
from app.models.order_item import OrderItem


class OrderItemAdmin(ModelView, model=OrderItem):
    column_list = [
        OrderItem.ingredient,
        OrderItem.amount,
        OrderItem.consumer,
        OrderItem.producer
    ]
    can_edit = False
    category = "directory"
