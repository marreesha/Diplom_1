import pytest
from praktikum.database import Database

BUN_NAMES = ['black bun', 'white bun', 'red bun']
SAUCE_NAMES = ['hot sauce', 'sour cream', 'chili sauce']
FILLING_NAMES = ['cutlet', 'dinosaur', 'sausage']


class TestDatabase:

    @classmethod
    def setup_class(cls):
        db = Database()
        cls.buns = {bun.name for bun in db.available_buns()}
        cls.ingredients = {ingredient.name for ingredient in db.available_ingredients()}

    @classmethod
    def teardown_class(cls):
        pass

    def test_available_buns_correct_quantity(self):
        assert len(self.buns) == 3

    @pytest.mark.parametrize('name', BUN_NAMES)
    def test_available_buns_bun_in_list(self, name):
        assert name in self.buns

    def test_available_ingredients_correct_quantity(self):
        assert len(self.ingredients) == 6

    @pytest.mark.parametrize('name', SAUCE_NAMES)
    def test_available_ingredients_sauce_in_list(self, name):
        assert name in self.ingredients

    @pytest.mark.parametrize('name', FILLING_NAMES)
    def test_available_ingredients_filling_in_list(self, name):
        assert name in self.ingredients
