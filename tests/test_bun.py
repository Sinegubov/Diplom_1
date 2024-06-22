from praktikum.bun import Bun


class TestBun:
    def test_bun_name(self, name, price):
        bun = Bun(name, price)

        assert bun.name == name
        assert bun.get_name() == name

    def test_bun_price(self, name, price):
        bun = Bun(name, price)

        assert bun.price == price
        assert bun.get_price() == price
