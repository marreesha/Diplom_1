import pytest
from praktikum.bun import Bun

NAME_AND_PRICE = [
    ('Asteroid XXL', 100),
    ('НеоГалактика', 200),
    ('Орбитальный обед', 300)
]


class TestBun:
    @pytest.mark.parametrize("name, price", NAME_AND_PRICE)
    def test_get_name_correct_name_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", NAME_AND_PRICE)
    def test_get_price_correct_price_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
