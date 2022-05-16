import datetime
from collections import namedtuple
from cashier.cash_register.tax_office import TaxOffice

PriceInfo = namedtuple('PriceInfo', 'price tax')

class Receipt:
    def __init__(self, items=None):
        self.time = datetime.datetime.now()
        self.items = dict() if items is None else items
        self.total_sales_tax = 0
        self.total_price = 0

    def add_item(self, item, sales_tax_rate):
        price = item.price * item.quantity
        sales_tax = price * sales_tax_rate
        taxed_price = price + sales_tax
        # TODO: handle when item already exists
        self.items[item] = PriceInfo(taxed_price, sales_tax)
    
    def remove_item(self, item):
        del self.items[item]

    def finish_receipt(self):
        total_sales_tax = 0
        total_price = 0
        for taxed_price, sales_tax in self.items.values():
            total_sales_tax += sales_tax
            total_price += taxed_price
        self.total_price = total_price
        self.total_sales_tax = total_sales_tax

    def get_items(self):
        return self.items


class Register:
    def __init__(self):
        self.reset()

    def process_item(self, item):
        if self.receipt is None:
            self.receipt = Receipt()
        tax_rate = TaxOffice.calculate_tax_rate(category=item.category, imported=item.imported)
        self.receipt.add_item(item, tax_rate)

    def delete_item(self, item):
        if self.receipt is not None:
            self.receipt.remove_item(item)

    def get_receipt(self):
        if self.receipt is not None:
            self.receipt.finish_receipt()
        return self.receipt

    def reset(self):
        self.receipt = None

