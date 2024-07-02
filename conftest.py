import pytest

from helpers.generator import Generator


@pytest.fixture(scope="function")
def name():
    name = Generator().generate_random_string_name()
    return name


@pytest.fixture(scope="function")
def price():
    price = Generator().generate_random_float()
    return price


@pytest.fixture(scope="function")
def type_ingredient():
    random_type = Generator().random_choice_of_ingredients()
    return random_type
