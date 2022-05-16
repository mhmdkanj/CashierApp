import pytest
from cashier.cash_register.register import Receipt, PriceInfo
from cashier.cash_register.item import Item
from cashier.cash_register.tax_office import ItemCategory

class TestReceipt:
    @pytest.fixture
    def empty_receipt(self):
        return Receipt()

    @pytest.fixture
    def basic_items(self):
        return (
            Item(name="item1", category=ItemCategory.NON_ESSENTIAL, price=100, quantity=2),
            Item(name="item1", category=ItemCategory.NON_ESSENTIAL, price=50, quantity=3),
        )

    @pytest.fixture
    def valid_receipt(self, basic_items):
        item1, item2 = basic_items
        items = {
            item1: PriceInfo(150, 50),
            item2: PriceInfo(55, 5)
        }
        return Receipt(items=items)

    def test_init(self, empty_receipt):
        receipt = empty_receipt
        assert len(receipt.get_items()) == 0
        assert receipt.total_sales_tax == 0
        assert receipt.total_price == 0

    def test_add_item(self, empty_receipt, basic_items):
        receipt = empty_receipt
        item1, _ = basic_items
        assert len(receipt.items) == 0
        assert receipt.total_sales_tax == 0
        assert receipt.total_price == 0
        receipt.add_item(item1, 0.1)
        assert receipt.items[item1] == (220, 20)

    def test_remove_tem(self, valid_receipt, basic_items):
        receipt = valid_receipt
        item1 = basic_items[0]
        assert len(receipt.items) == 2 and item1 in receipt.items
        receipt.remove_item(item1)
        assert len(receipt.items) == 1 and item1 not in receipt.items
 
        