'''
Integration Tests
'''
import pytest
from cashier.cash_register.register import Register
from cashier.cash_register.item import Item
from cashier.cash_register.tax_office import ItemCategory


class TestCashier:
    @pytest.fixture
    def get_register(self):
        return Register()

    def test_input_1(self, get_register):
        register = get_register
        item1 = Item(name="book", price=12.49, category=ItemCategory.BOOK, quantity=1, imported=False)
        item2 = Item(name="music CD", price=14.99, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=False)
        item3 = Item(name="chocolate bar", price=0.85, category=ItemCategory.FOOD, quantity=1, imported=False)
        register.process_item(item1)
        register.process_item(item2)
        register.process_item(item3)

        receipt = register.get_receipt()
        items = receipt.get_items()

        assert len(items) == 3
        assert items[item1] == (12.49, 0)
        assert items[item2] == (16.49, 1.5)
        assert items[item3] == (0.85, 0)
        assert receipt.total_sales_tax == 1.5
        assert receipt.total_price == 29.83

    def test_input_2(self, get_register):
        register = get_register
        item1 = Item(name="box of chocolates", price=10.00, category=ItemCategory.FOOD, quantity=1, imported=True)
        item2 = Item(name="bottle of perfume", price=47.50, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=True)
        register.process_item(item1)
        register.process_item(item2)

        receipt = register.get_receipt()
        items = receipt.get_items()

        assert len(items) == 2
        assert items[item1] == (10.5, 0.5)
        assert items[item2] == (54.65, 7.15)
        assert receipt.total_sales_tax == 7.65
        assert receipt.total_price == 65.15

    def test_input_3(self, get_register):
        register = get_register
        item1 = Item(name="bottle of perfume", price=27.99, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=True)
        item2 = Item(name="bottle of perfume", price=18.99, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=False)
        item3 = Item(name="packet of headache pills", price=9.75, category=ItemCategory.MEDICAL, quantity=1, imported=False)
        item4 = Item(name="box of chocolates", price=11.25, category=ItemCategory.FOOD, quantity=1, imported=True)
        register.process_item(item1)
        register.process_item(item2)
        register.process_item(item3)
        register.process_item(item4)

        receipt = register.get_receipt()
        items = receipt.get_items()

        assert len(items) == 4
        assert items[item1] == (32.19, 4.20)
        assert items[item2] == (20.89, 1.90)
        assert items[item3] == (9.75, 0)
        assert items[item4] == (11.85, 0.60)
        assert receipt.total_sales_tax == 6.70
        assert receipt.total_price == 74.68

    def test_input_4(self, get_register):
        register = get_register
        item1 = Item(name="bottle of perfume", price=27.99, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=True)
        item2 = Item(name="bottle of perfume", price=18.99, category=ItemCategory.NON_ESSENTIAL, quantity=2, imported=False)
        item3 = Item(name="packet of headache pills", price=9.75, category=ItemCategory.MEDICAL, quantity=3, imported=False)
        item4 = Item(name="box of chocolates", price=11.25, category=ItemCategory.FOOD, quantity=4, imported=True)
        register.process_item(item1)
        register.process_item(item2)
        register.process_item(item3)
        register.process_item(item4)

        receipt = register.get_receipt()
        items = receipt.get_items()

        assert len(items) == 4
        assert items[item1] == (32.19, 4.20)
        assert items[item2] == (41.78, 3.80)
        assert items[item3] == (29.25, 0)
        assert items[item4] == (47.25, 2.25)
        assert receipt.total_sales_tax == 10.25
        assert receipt.total_price == 150.47
