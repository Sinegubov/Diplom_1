import random
import faker

from praktikum.ingredient_types import *


class Generator:
    @staticmethod
    def generate_random_float():
        return random.uniform(0.0, 999.99)

    @staticmethod
    def generate_random_string_name():
        return faker.Faker().name()

    @staticmethod
    def random_choice_of_ingredients():
        types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
        random_type = random.choice(types)
        return random_type
