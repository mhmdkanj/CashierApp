from cashier.cash_register.register import Register
from cashier.cash_register.item import Item
from cashier.cash_register.tax_office import ItemCategory
from cashier.cash_register.utils import ReceiptPrinter


def main():
    register = Register()

    # Input 1
    print("+++++++++++++++++ Input 1 +++++++++++++++++")
    item1 = Item(name="book", price=12.49, category=ItemCategory.BOOK, quantity=1, imported=False)
    item2 = Item(name="music CD", price=14.99, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=False)
    item3 = Item(name="chocolate bar", price=0.85, category=ItemCategory.FOOD, quantity=1, imported=False)
    register.process_item(item1)
    register.process_item(item2)
    register.process_item(item3)

    receipt = register.get_receipt()
    ReceiptPrinter.print_receipt(receipt)

    # Input 2
    print("+++++++++++++++++ Input 2 +++++++++++++++++")
    item1 = Item(name="box of chocolates", price=10.00, category=ItemCategory.FOOD, quantity=1, imported=True)
    item2 = Item(name="bottle of perfume", price=47.50, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=True)
    register.process_item(item1)
    register.process_item(item2)

    receipt = register.get_receipt()
    ReceiptPrinter.print_receipt(receipt)

    # Input 3
    print("+++++++++++++++++ Input 3 +++++++++++++++++")
    item1 = Item(name="bottle of perfume", price=27.99, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=True)
    item2 = Item(name="bottle of perfume", price=18.99, category=ItemCategory.NON_ESSENTIAL, quantity=1, imported=False)
    item3 = Item(name="packet of headache pills", price=9.75, category=ItemCategory.MEDICAL, quantity=1, imported=False)
    item4 = Item(name="box of chocolates", price=11.25, category=ItemCategory.FOOD, quantity=1, imported=True)
    register.process_item(item1)
    register.process_item(item2)
    register.process_item(item3)
    register.process_item(item4)

    receipt = register.get_receipt()
    ReceiptPrinter.print_receipt(receipt)


if __name__ == '__main__':
    main()
