from pydantic.main import BaseModel

from app.serializers.ingredient import IngredientModel
from app.serializers.product import ProductSerializer


class ProductIngredientAssociationSerializer(BaseModel):
    product_id: int
    ingredient_id: int
    nominal_coefficient: float
    ingredient: IngredientModel
    product: ProductSerializer
