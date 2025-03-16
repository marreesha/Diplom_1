import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from helpers import *


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    def _set_bun(bun_data):
        bun = Mock()
        bun.get_name.return_value = bun_data[0]
        bun.get_price.return_value = bun_data[1]
        return bun

    return _set_bun


@pytest.fixture
def mock_ingredient():
    def _set_ingredient(ingredient_data):
        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_data[0]
        ingredient.get_name.return_value = ingredient_data[1]
        ingredient.get_price.return_value = ingredient_data[2]
        return ingredient

    return _set_ingredient


@pytest.fixture
def setup_ingredients(burger, mock_ingredient):
    def _add_ingredient(ingredient_quantity):
        ingredient_mock_list = []
        for _ in range(ingredient_quantity):
            ingredient_data = generate_ingredient_data()
            print(f'Ingredient: type={ingredient_data[0]}, name={ingredient_data[1]}, price={ingredient_data[2]}')

            ingredient_mock = mock_ingredient(ingredient_data)
            ingredient_mock_list.append(ingredient_mock)
            burger.add_ingredient(ingredient_mock)
        return ingredient_mock_list

    return _add_ingredient
