from enum import Enum


class ItemCategory(Enum):
    OTHER = 0
    FOOD = 1
    BOOK = 2
    MEDICAL = 3


class Item:
    def __init__(self, name, price, category, quantity=1, imported=False):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        self.imported = imported

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if not isinstance(val, (int, float)):
            raise ValueError(f"Price for item {self.name} should be a number.")
        if val < 0:
            raise ValueError(f"Price for item {self.name} cannot be negative.")
        self._price = val

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, price={self.price}, category={self.category}, quantity={self.quantity}, imported={self.imported})"

    def __str__(self):
        return f"{self.name} x{self.quantity}"