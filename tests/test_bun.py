import pytest
from bun import Bun


class TestBun:
    @pytest.mark.parametrize("bun_name, bun_price", [
        ("BigBun", 1),
        ("123", 0),
        ("", -1),
        ("Другая раскладка", 1.0)
                ])
    def test_bun_name(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.name == bun_name and bun.price == bun_price
