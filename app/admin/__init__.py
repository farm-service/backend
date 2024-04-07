from app.admin.units_of_measurement import UnitOfMeasurementAdmin
from app.admin.user import UserAdmin
from app.admin.ingredients import IngredientAdmin
from app.admin.role import RoleAdmin
from app.admin.product_ingredient_association import ProductIngredientAssociationAdmin
from app.admin.product import ProductAdmin

# TODO automate class collection

__all__ = [
    UserAdmin,
    IngredientAdmin,
    ProductAdmin,
    UnitOfMeasurementAdmin,
    RoleAdmin,
    ProductIngredientAssociationAdmin
]
