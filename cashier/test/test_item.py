import pytest
from cashier.cash_register.item import Item, ItemCategory


class TestItem:

    @pytest.fixture
    def basic_item(self):
        return Item(name="x", price=1.5, category=ItemCategory.OTHER)
    
    def test_init(self, basic_item):
        item = basic_item
        assert item.name == "x"
        assert item.price == 1.5
        assert item.category == ItemCategory.OTHER
        assert item.quantity == 1
        assert item.imported == False

    def test_price_invalid(self, basic_item):
        item = basic_item
        with pytest.raises(ValueError):
            item.price = 'invalid'

    def test_price_negative(self, basic_item):
        item = basic_item
        with pytest.raises(ValueError):
            item.price = -2
