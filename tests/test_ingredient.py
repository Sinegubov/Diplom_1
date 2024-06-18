import pytest
from ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type", ["Острый соус", "gorchitsa", ""])
    def test_ingredient_type(self, ingredient_type):
        type_ingr = Ingredient(ingredient_type, name='def_name_ingr', price=1).type
        assert type_ingr == ingredient_type

    @pytest.mark.parametrize("name", ["1000 Островов", "Tar-Tar", ""])
    def test_ingredient_name(self, name):
        name_ingr = Ingredient(ingredient_type="def_type_name", name=name, price=1).name
        assert name_ingr == name

    @pytest.mark.parametrize("price", [0, 666666, 1.23, -2])
    def test_ingredient_price(self, price):
        price_ingr = Ingredient(ingredient_type="def_type_name", name='def_name_ingr', price=price).price
        assert price_ingr == price
