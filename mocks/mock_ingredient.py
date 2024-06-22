from unittest.mock import Mock


def set_mock_ingredient(type_ingredient, name, price):
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = type_ingredient
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_price.return_value = price

    return mock_ingredient
