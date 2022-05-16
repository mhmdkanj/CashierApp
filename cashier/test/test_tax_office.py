from cashier.cash_register.tax_office import TaxOffice, ItemCategory


class TestTaxOffice:
    def test_calculate_tax_rate_non_essential(self):
        assert TaxOffice.calculate_tax_rate(category=ItemCategory.NON_ESSENTIAL, imported=False) == 0.10

    def test_calculate_tax_rate_essential(self):
        assert TaxOffice.calculate_tax_rate(category=ItemCategory.FOOD, imported=False) == 0
        assert TaxOffice.calculate_tax_rate(category=ItemCategory.BOOK, imported=False) == 0
        assert TaxOffice.calculate_tax_rate(category=ItemCategory.MEDICAL, imported=False) == 0

    def test_calculate_tax_rate_non_essential_imported(self):
        assert TaxOffice.calculate_tax_rate(category=ItemCategory.NON_ESSENTIAL, imported=True) == 0.15

    def test_calculate_tax_rate_essential_imported(self):
        assert TaxOffice.calculate_tax_rate(category=ItemCategory.FOOD, imported=True) == 0.05
        assert TaxOffice.calculate_tax_rate(category=ItemCategory.BOOK, imported=True) == 0.05
        assert TaxOffice.calculate_tax_rate(category=ItemCategory.MEDICAL, imported=True) == 0.05
