from typing import Optional, List

from sqlalchemy import Column, Integer, Float, ForeignKey, select
from sqlalchemy.orm import relationship, selectinload

from app.auth import get_async_session
from app.models import Ingredient, UnitOfMeasurement, Product
from app.models.base import Base
from app.serializers.ingredient import IngredientModel
from app.serializers.product import ProductSerializer
from app.serializers.product_ingredient_association import ProductIngredientAssociationSerializer
from app.serializers.units_of_measurement import UnitOfMeasurementSerializer


class ProductIngredientAssociation(Base):
    __tablename__ = 'product_ingredient_association'

    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    nominal_coefficient = Column(Float)

    product = relationship("Product", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="product")

    pydantic_serializer = ProductIngredientAssociationSerializer

    @classmethod
    async def get_items_by_product(cls, product_id: str) -> Optional[List[ProductIngredientAssociationSerializer]]:
        """
        Method returns items for recipe

        Args:
            product_id (str): id of product for recipe

        Returns:
            recipe Optional[List[ProductIngredientAssociationSerializer]]: List of recipes by product_id or None
        """
        result_list = list()
        try:
            async for session in get_async_session():
                query = select(ProductIngredientAssociation). \
                    join(Ingredient). \
                    join(UnitOfMeasurement). \
                    join(Product). \
                    options(
                        selectinload(ProductIngredientAssociation.ingredient).
                        selectinload(Ingredient.measure_unit),
                        selectinload(ProductIngredientAssociation.product)
                    ). \
                    filter(ProductIngredientAssociation.product_id == int(product_id))
                result = await session.execute(query)
                order_items: List[ProductIngredientAssociation] = result.scalars().all()
                for order_item in order_items:
                    ingredient_dict = order_item.ingredient.__dict__
                    unit_of_measurement_dict = order_item.ingredient.measure_unit.__dict__
                    product_dict = order_item.product.__dict__
                    unit_of_measurement_serialized_data = UnitOfMeasurementSerializer(**unit_of_measurement_dict)
                    ingredient_model = IngredientModel(
                        id=ingredient_dict.get('id'),
                        name=ingredient_dict.get('name'),
                        measure_unit_id=ingredient_dict.get('measure_unit_id'),
                        measure_unit=unit_of_measurement_serialized_data
                    )
                    product_serialized_data = ProductSerializer(
                        id=product_dict.get('id'),
                        name=product_dict.get('name'),
                        owner_id=product_dict.get('owner_id')
                    )
                    result_list.append(
                        ProductIngredientAssociationSerializer(
                            product_id=order_item.product_id,
                            ingredient_id=order_item.ingredient_id,
                            nominal_coefficient=order_item.nominal_coefficient,
                            ingredient=ingredient_model,
                            product=product_serialized_data
                        )
                    )
            return result_list
        except Exception as e:
            print(f'Exception query: {e}')
