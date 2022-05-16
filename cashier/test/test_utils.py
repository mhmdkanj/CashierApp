from cashier.cash_register.utils import truncate

class TestUtils:
    def test_truncate(self):
        assert truncate(16.4900000000002) == 16.49
        assert truncate(16.491) == 16.49
        assert truncate(16.499) == 16.5
        assert truncate(16.40) == 16.4
        assert truncate(16) == 16
