import datetime
from collections import namedtuple

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