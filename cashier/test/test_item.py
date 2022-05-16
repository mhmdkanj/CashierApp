import pytest
from cashier.cash_register.item import Item
from cashier.cash_register.tax_office import ItemCategory


class TestItem:

    @pytest.fixture
    def basic_item(self):
        return Item(name="x", price=1.5, category=ItemCategory.NON_ESSENTIAL)

    def test_init(self, basic_item):
        item = basic_item
        assert item.name == "x"
        assert item.price == 1.5
        assert item.category == ItemCategory.NON_ESSENTIAL
        assert item.quantity == 1
        assert not item.imported

    def test_price_invalid(self, basic_item):
        item = basic_item
        with pytest.raises(ValueError):
            item.price = 'invalid'

    def test_price_negative(self, basic_item):
        item = basic_item
        with pytest.raises(ValueError):
            item.price = -2
