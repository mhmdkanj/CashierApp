import math
import datetime
from collections import namedtuple
from cashier.cash_register.tax_office import TaxOffice

PriceInfo = namedtuple('PriceInfo', 'price tax')


def truncate(number):
    # enough to truncate numbers up to two decimal places taking into consideration float storage errors
    return round(number, 2)


class Receipt:
    def __init__(self, items=None):
        self.time = datetime.datetime.now()
        self.items = dict() if items is None else items
        self.total_sales_tax = 0
        self.total_price = 0

    def add_item(self, item, price, sales_tax):
        taxed_price = truncate(price + sales_tax)  # truncate trailing float error
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
        self.total_price = truncate(total_price)
        self.total_sales_tax =  truncate(total_sales_tax)

    def get_items(self):
        return self.items


class Register:
    def __init__(self):
        self.reset()

    def process_item(self, item):
        if self.receipt is None:
            self.receipt = Receipt()
        tax_rate = TaxOffice.calculate_tax_rate(category=item.category, imported=item.imported)
        price = item.price * item.quantity
        sales_tax = price * tax_rate
        sales_tax = self.round_up(sales_tax)

        self.receipt.add_item(item, price, sales_tax)

    def delete_item(self, item):
        if self.receipt is not None:
            self.receipt.remove_item(item)

    def get_receipt(self):
        if self.receipt is not None:
            self.receipt.finish_receipt()
        receipt = self.receipt
        self.reset()
        return receipt

    def reset(self):
        self.receipt = None

    @staticmethod
    def round_up(number, fraction=0.05):
        # round number up to nearest fraction
        rounded_up = math.ceil(number / fraction) * fraction
        # truncate rounded number so that only two decimal places remain
        return round(rounded_up, -int(math.floor(math.log10(fraction))))
