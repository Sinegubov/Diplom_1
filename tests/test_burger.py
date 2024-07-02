import pytest

from helpers.generator import Generator
from praktikum.ingredient_types import *
from mocks.mock_ingredient import *
from praktikum.burger import Burger
from data import DataTestBurger
from mocks.mock_bun import *


class TestBurger:
    def test_set_buns(self, name, price):
        mock_bun = set_mock_bun(name, price)
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.get_name() == name and burger.bun.get_price() == price

    @pytest.mark.parametrize("type_name", [[INGREDIENT_TYPE_SAUCE], [INGREDIENT_TYPE_FILLING]])
    def test_add_ingredient(self, name, price, type_name):
        mock_ingredient = set_mock_ingredient(type_name, name, price)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, name, price, type_ingredient):
        mock_ingredient_1 = set_mock_ingredient(type_ingredient, name, price)
        mock_ingredient_2 = set_mock_ingredient(type_ingredient, name, price)
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_2

    def test_move_ingredient(self, name, price, type_ingredient):
        mock_ingredient_1 = set_mock_ingredient(type_ingredient, name, price)
        mock_ingredient_2 = set_mock_ingredient(type_ingredient, name, price)
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient_1

    def test_get_price(self, name, price, type_ingredient):
        price_bun = Generator().generate_random_float()
        price_ingredient = Generator().generate_random_float()
        calculate_price = price_bun*2 + price_ingredient

        mock_bun = set_mock_bun(name, price=price_bun)
        mock_ingredient = set_mock_ingredient(type_ingredient, name, price=price_ingredient)
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == calculate_price

    def test_get_receipt(self):
        mock_bun = set_mock_bun(
            name=DataTestBurger.bun_name,
            price=DataTestBurger.bun_price)
        mock_ingredient_1 = set_mock_ingredient(
            type_ingredient=DataTestBurger.ingredient_type_1,
            name=DataTestBurger.ingredient_name_1,
            price=DataTestBurger.ingredient_price_1)
        mock_ingredient_2 = set_mock_ingredient(
            type_ingredient=DataTestBurger.ingredient_type_2,
            name=DataTestBurger.ingredient_name_2,
            price=DataTestBurger.ingredient_price_2)

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        assert burger.get_receipt() == DataTestBurger.expected_receipt
