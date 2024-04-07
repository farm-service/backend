from sqladmin import ModelView
from app.models.ingredient import Ingredient


class IngredientAdmin(ModelView, model=Ingredient):
    column_list = [
        Ingredient.id,
        Ingredient.name,
        Ingredient.measure_unit_id,
        Ingredient.measure_unit
    ]

    category = "directory"
