import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

TYPE_NAME_PRICE = [
    (INGREDIENT_TYPE_SAUCE, 'Плазменный соус', 400),
    (INGREDIENT_TYPE_FILLING, 'Космическая пыль', 700),
    (INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
    (INGREDIENT_TYPE_FILLING, 'cutlet', 100)
]


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', TYPE_NAME_PRICE)
    def test_get_type_correct_type_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type, name, price', TYPE_NAME_PRICE)
    def test_get_name_correct_name_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', TYPE_NAME_PRICE)
    def test_get_price_correct_price_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
