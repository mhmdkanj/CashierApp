from cashier.cash_register.utils import truncate


class Item:
    def __init__(self, name, price, category, quantity=1, imported=False):
        self.name = name
        self.quantity = quantity
        self.price = price  # price per one item
        self.category = category  # one of ItemCategory
        self.imported = imported

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        # allow number inputs only
        if not isinstance(val, (int, float)):
            raise ValueError(f"Price for item {self.name} should be a number.")
        # allow non-negative inputs only
        elif val < 0:
            raise ValueError(f"Price for item {self.name} cannot be negative.")
        self._price = val

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, price={self.price}, category={self.category}, quantity={self.quantity}, imported={self.imported})"

    def __str__(self):
        return f"{self.quantity}x {self.name}"

    def __hash__(self):
        uid = "imported " + self.name if self.imported else self.name
        return hash(uid)