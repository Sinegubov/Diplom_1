import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    @pytest.mark.parametrize("type_name", [[INGREDIENT_TYPE_SAUCE], [INGREDIENT_TYPE_FILLING]])
    def test_ingredient_type(self, name, price, type_name):
        ingredient = Ingredient(ingredient_type=type_name, name=name, price=price)
        type_ingredient = ingredient.type

        assert type_ingredient == type_name
        assert ingredient.get_type() == type_name

    def test_ingredient_name(self, name, price, type_ingredient):
        ingredient = Ingredient(ingredient_type=type_ingredient, name=name, price=price)
        name_ingredient = ingredient.name

        assert name_ingredient == name
        assert ingredient.get_name() == name

    def test_ingredient_price(self, name, price, type_ingredient):
        ingredient = Ingredient(ingredient_type=type_ingredient, name=name, price=price)
        price_ingredient = ingredient.price

        assert price_ingredient == price
        assert ingredient.get_price() == price
