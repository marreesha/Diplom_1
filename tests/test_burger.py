import pytest
import random
from helpers import *
from conftest import burger, mock_bun, mock_ingredient, setup_ingredients

INGREDIENT_QUANTITY = (1, 3, 6, 10)


class TestBurger:

    @pytest.mark.repeat(2)
    def test_set_buns(self, burger, mock_bun):
        bun_data = generate_bun_data()

        bun = mock_bun(bun_data)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_add_one(self, burger, mock_ingredient):
        ingredient_data = generate_ingredient_data()

        ingredient = mock_ingredient(ingredient_data)
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize("ingredient_quantity", (0, 3, 6, 10))
    def test_add_ingredient_add_several(self, burger, setup_ingredients, ingredient_quantity):
        ingredient_mock_list = setup_ingredients(ingredient_quantity)

        assert len(burger.ingredients) == ingredient_quantity
        assert burger.ingredients == ingredient_mock_list

    @pytest.mark.parametrize("ingredient_quantity", (1, 3, 6, 10))
    def test_remove_ingredient_existing_ingredients(self, burger, setup_ingredients, ingredient_quantity):
        ingredient_mock_list = setup_ingredients(ingredient_quantity)

        # выбираем индекс ингредиента
        index = random.randint(0, ingredient_quantity - 1)

        # удаляем ингредиент
        burger.remove_ingredient(index)

        assert len(burger.ingredients) == ingredient_quantity - 1
        assert ingredient_mock_list[index] not in burger.ingredients

    @pytest.mark.parametrize("ingredient_quantity", (2, 3, 6, 10))
    def test_move_ingredient(self, burger, setup_ingredients, ingredient_quantity):
        ingredient_mock_list = setup_ingredients(ingredient_quantity)

        # выбираем индекс ингредиента
        old_index, new_index = random.sample(range(0, ingredient_quantity), 2)

        # перемещаем ингредиент
        burger.move_ingredient(old_index, new_index)

        assert len(burger.ingredients) == ingredient_quantity
        assert burger.ingredients[new_index] == ingredient_mock_list[old_index]

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        bun, ingredient = mock_bun(generate_bun_data()), mock_ingredient(generate_ingredient_data())

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 2 * bun.get_price() + ingredient.get_price()

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        bun, ingredient = mock_bun(generate_bun_data()), mock_ingredient(generate_ingredient_data())

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'(==== {bun.get_name()} ====)\n= {ingredient.get_type().lower()} {ingredient.get_name()} =\n(==== {bun.get_name()} ====)\n\nPrice: {burger.get_price()}'

        assert burger.get_receipt() == expected_receipt
