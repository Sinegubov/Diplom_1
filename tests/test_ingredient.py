import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type", ["SAUCE", "FILLING"])
    def test_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, name="onion", price=1)
        type_ingredient = ingredient.type
        assert type_ingredient == ingredient_type
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["1000 Островов", "Tar-Tar", ""])
    def test_ingredient_name(self, name):
        ingredient = Ingredient(ingredient_type="SAUCE", name=name, price=1)
        name_ingredient = ingredient.name
        assert name_ingredient == name
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [0, 666666, 1.23, -2])
    def test_ingredient_price(self, price):
        ingredient = Ingredient(ingredient_type="FILLING", name="onion", price=price)
        price_ingredient = ingredient.price
        assert price_ingredient == price
        assert ingredient.get_price() == price
