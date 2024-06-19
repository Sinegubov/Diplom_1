from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_initialization(self):
        db = Database()
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6

        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ]

        for bun, (name, price) in zip(db.buns, expected_buns):
            assert bun.get_name() == name
            assert bun.get_price() == price

        expected_ingredients = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]

        for ingredient, (type_, name, price) in zip(db.ingredients, expected_ingredients):
            assert ingredient.get_type() == type_
            assert ingredient.get_name() == name
            assert ingredient.get_price() == price

    def test_available_buns(self):
        db = Database()
        available_buns = db.available_buns()
        assert len(available_buns) == 3
        assert available_buns[0].get_name() == "black bun"
        assert available_buns[1].get_name() == "white bun"
        assert available_buns[2].get_name() == "red bun"

    def test_available_ingredients(self):
        db = Database()
        available_ingredients = db.available_ingredients()
        assert len(available_ingredients) == 6
        assert available_ingredients[0].get_name() == "hot sauce"
        assert available_ingredients[1].get_name() == "sour cream"
        assert available_ingredients[2].get_name() == "chili sauce"
        assert available_ingredients[3].get_name() == "cutlet"
        assert available_ingredients[4].get_name() == "dinosaur"
        assert available_ingredients[5].get_name() == "sausage"
