from sqladmin import ModelView
from app.models.product_ingredient_association import ProductIngredientAssociation


class ProductIngredientAssociationAdmin(ModelView, model=ProductIngredientAssociation):
    column_list = [
        ProductIngredientAssociation.product_id,
        ProductIngredientAssociation.product,
        ProductIngredientAssociation.ingredient_id,
        ProductIngredientAssociation.ingredient,
        ProductIngredientAssociation.nominal_coefficient
    ]
    form_widget_args = {
        "product": {
            "readonly": True,
        },
        "ingredient": {
            "readonly": True,
        },
    }

    category = "directory"
