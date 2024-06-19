import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        bun = Bun(name="CrastyCrabs", price=1.5)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        ingredient = Ingredient(ingredient_type="FILLING", name='def_name_ingr', price=1.5)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        ingredient1 = Ingredient(ingredient_type="SAUCE", name='Tar-Tar', price=0.5)
        ingredient2 = Ingredient(ingredient_type="FILLING", name='onion', price=1.5)
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        ingredient1 = Ingredient(ingredient_type="SAUCE", name='Tar-Tar', price=0.5)
        ingredient2 = Ingredient(ingredient_type="FILLING", name='onion', price=1.5)
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        bun = Bun(name="CrastyCrabs", price=1.5)
        ingredient1 = Ingredient(ingredient_type="SAUCE", name='Tar-Tar', price=0.5)
        ingredient2 = Ingredient(ingredient_type="FILLING", name='onion', price=1.5)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 5.0  # 1.5*2 + 0.5 + 1.5

    def test_get_receipt(self):
        bun = Bun(name="CrastyCrabs", price=1.5)
        ingredient1 = Ingredient(ingredient_type="SAUCE", name='Tar-Tar', price=0.5)
        ingredient2 = Ingredient(ingredient_type="FILLING", name='onion', price=1.5)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_receipt = (
            "(==== CrastyCrabs ====)\n"
            "= sauce Tar-Tar =\n"
            "= filling onion =\n"
            "(==== CrastyCrabs ====)\n\n"
            "Price: 5.0"
        )
        assert burger.get_receipt() == expected_receipt
