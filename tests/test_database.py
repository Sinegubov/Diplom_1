from praktikum.database import Database
from data import DataDatabaseTestBurger


class TestDatabase:
    def test_available_buns(self):
        db = Database()
        available_buns = db.available_buns()

        assert len(available_buns) == 3
        assert available_buns[0].get_name() == DataDatabaseTestBurger.expected_buns[0][0]
        assert available_buns[1].get_name() == DataDatabaseTestBurger.expected_buns[1][0]
        assert available_buns[2].get_name() == DataDatabaseTestBurger.expected_buns[2][0]

    def test_available_ingredients(self):
        db = Database()
        available_ingredients = db.available_ingredients()

        assert len(available_ingredients) == 6
        assert available_ingredients[0].get_name() == DataDatabaseTestBurger.expected_ingredients[0][0]
        assert available_ingredients[1].get_name() == DataDatabaseTestBurger.expected_ingredients[1][0]
        assert available_ingredients[2].get_name() == DataDatabaseTestBurger.expected_ingredients[2][0]
        assert available_ingredients[3].get_name() == DataDatabaseTestBurger.expected_ingredients[3][0]
        assert available_ingredients[4].get_name() == DataDatabaseTestBurger.expected_ingredients[4][0]
        assert available_ingredients[5].get_name() == DataDatabaseTestBurger.expected_ingredients[5][0]
