import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("bun_name", ["BigBun", "123", "", "Бургер по-русски"])
    def test_bun_name(self, bun_name):
        bun = Bun(name=bun_name, price=1)
        assert bun.name == bun_name
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize("bun_price", [1.0, 0.0, -0.1, 500])
    def test_bun_price(self, bun_price):
        bun = Bun(name="BUN", price=bun_price)
        assert bun.price == bun_price
        assert bun.get_price() == bun_price
