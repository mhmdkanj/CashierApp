import pytest
from pytest_mock import mocker
from cashier.cash_register.register import Receipt, Register, PriceInfo
from cashier.cash_register.item import Item
from cashier.cash_register.tax_office import ItemCategory


@pytest.fixture
def basic_items():
    return (
        Item(name="item1", category=ItemCategory.NON_ESSENTIAL, price=100, quantity=2),
        Item(name="item1", category=ItemCategory.NON_ESSENTIAL, price=50, quantity=3),
    )


class TestReceipt:
    @pytest.fixture
    def empty_receipt(self):
        return Receipt()

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
        receipt.add_item(item1, 200, 20)
        assert receipt.items[item1] == (220, 20)

    def test_remove_item(self, valid_receipt, basic_items):
        receipt = valid_receipt
        item1 = basic_items[0]
        assert len(receipt.items) == 2 and item1 in receipt.items
        receipt.remove_item(item1)
        assert len(receipt.items) == 1 and item1 not in receipt.items

    def test_finish_receipt(self, valid_receipt):
        receipt = valid_receipt
        assert receipt.total_sales_tax == 0
        assert receipt.total_price == 0
        receipt.finish_receipt()
        assert receipt.total_price == 205
        assert receipt.total_sales_tax == 55


class TestRegister:
    @pytest.fixture
    def basic_register(self):
        return Register()

    @pytest.fixture
    def valid_register(self):
        register = Register()
        register.receipt = Receipt()
        return register

    def test_init(self, basic_register):
        register = basic_register
        assert register.receipt is None

    def test_get_receipt_empty(self, basic_register):
        register = basic_register
        assert register.get_receipt() is None

    def test_process_item(self, basic_register, basic_items, mocker):
        register = basic_register
        item1 = basic_items[0]
        receipt_mocker = mocker.patch('cashier.cash_register.register.Receipt')
        import cashier
        calculate_tax_rate_mocker = mocker.patch.object(cashier.cash_register.tax_office.TaxOffice, 'calculate_tax_rate')
        calculate_tax_rate_mocker.return_value = 0.1
        # call first time
        register.process_item(item1)
        receipt_mocker.assert_called_once()
        calculate_tax_rate_mocker.assert_called_once_with(category=item1.category, imported=item1.imported)
        receipt_mocker().add_item.assert_called_once_with(item1, 200, 20)

    def test_process_item_ongoing(self, basic_register, basic_items, mocker):
        register = basic_register
        item1 = basic_items[0]
        receipt_mocker = mocker.patch('cashier.cash_register.register.Receipt')
        register.receipt = receipt_mocker
        import cashier
        calculate_tax_rate_mocker = mocker.patch.object(cashier.cash_register.tax_office.TaxOffice, 'calculate_tax_rate')
        calculate_tax_rate_mocker.return_value = 0.1
        # call with existing receipt
        register.process_item(item1)
        receipt_mocker.assert_not_called()
        calculate_tax_rate_mocker.assert_called_once_with(category=item1.category, imported=item1.imported)
        receipt_mocker.add_item.assert_called_once_with(item1, 200, 20)

    def test_delete_item(self, basic_register, basic_items, mocker):
        register = basic_register
        item1 = basic_items[0]
        receipt_mocker = mocker.patch('cashier.cash_register.register.Receipt')
        register.delete_item(item1)
        receipt_mocker.assert_not_called()

    def test_delete_item_existing(self, basic_register, basic_items, mocker):
        register = basic_register
        item1 = basic_items[0]
        receipt_mocker = mocker.patch('cashier.cash_register.register.Receipt')
        register.receipt = receipt_mocker
        register.delete_item(item1)
        receipt_mocker.remove_item.assert_called_once_with(item1)

    def test_reset(self, basic_register):
        register = basic_register
        register.reset()
        assert register.receipt is None

    def test_reset_existing(self, basic_register, mocker):
        register = basic_register
        receipt_mocker = mocker.patch('cashier.cash_register.register.Receipt')
        register.receipt = receipt_mocker
        assert register.receipt is not None
        register.reset()
        assert register.receipt is None

    def test_round_up(self):
        assert Register.round_up(35.10) == 35.10
        assert Register.round_up(35.11) == 35.15
        assert Register.round_up(35.13) == 35.15
        assert Register.round_up(35.15) == 35.15
        assert Register.round_up(35.16) == 35.20
        assert Register.round_up(35.19) == 35.20

    def test_round_up_precise(self):
        assert Register.round_up(35.1000) == 35.10
        assert Register.round_up(35.1152) == 35.15
        assert Register.round_up(35.1321) == 35.15
        assert Register.round_up(35.150) == 35.15
        assert Register.round_up(35.1693) == 35.20
        assert Register.round_up(35.19) == 35.20
