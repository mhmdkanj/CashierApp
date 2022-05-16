from enum import Enum
from cashier.cash_register.utils import truncate


class ItemCategory(Enum):
    NON_ESSENTIAL = 0
    FOOD = 1
    BOOK = 2
    MEDICAL = 3


class TaxOffice:
    """Tax rate calculator."""

    @staticmethod
    def calculate_tax_rate(category, imported):
        sales_tax_rate = 0
        # +5% on imported items
        if imported:
            sales_tax_rate += 0.05
        # +10% on non-essential items
        if category == ItemCategory.NON_ESSENTIAL:
            sales_tax_rate += 0.1
        return truncate(sales_tax_rate)
