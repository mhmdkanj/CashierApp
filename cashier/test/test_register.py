import pytest
from cashier.cash_register.register import Receipt
from cashier.cash_register.item import Item
from cashier.cash_register.tax_office import ItemCategory

class TestReceipt:
    @pytest.fixture
    def empty_receipt(self):
        return Receipt()

    @pytest.fixture
    def basic_item(self):
        return Item(name="item1", category=ItemCategory.NON_ESSENTIAL, price=100, quantity=2)
       
    def test_init(self, empty_receipt):
        receipt = empty_receipt
        assert len(receipt.get_items()) == 0
        assert receipt.total_sales_tax == 0
        assert receipt.total_price == 0

    def test_init(self, empty_receipt, basic_item):
        receipt = empty_receipt
        item1 = basic_item

        assert len(receipt.get_items()) == 0
        assert receipt.total_sales_tax == 0
        assert receipt.total_price == 0

        receipt.add_item(item1, 0.1)

        assert receipt.get_items()[item1] == (220, 20)
        
