from enum import Enum


class ItemCategory(Enum):
    NON_ESSENTIAL = 0
    FOOD = 1
    BOOK = 2
    MEDICAL = 3


class TaxOffice:
    @staticmethod
    def calculate_tax_rate(category, imported):
        sales_tax_rate = 0
        if imported:
            sales_tax_rate += 0.05
        if category == ItemCategory.NON_ESSENTIAL:
            sales_tax_rate += 0.1
        return sales_tax_rate
