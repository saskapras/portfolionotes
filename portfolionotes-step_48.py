# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: PortfolioNotes
import unittest
from datetime import date, timedelta

def is_valid_date(d):
    return isinstance(d, date) and d > date(2000, 1, 1)

def is_valid_price(p):
    return isinstance(p, (int, float)) and p > 0

def is_valid_note(n):
    return isinstance(n, str) and 1 <= len(n) <= 500

def is_valid_holding(h):
    return (is_valid_date(h.get("date"))
            and is_valid_price(h.get("price", 0))
            and is_valid_note(h.get("note", ""))
            and isinstance(h.get("shares"), (int, float))
            and h["shares"] > 0
            and h.get("cost", 0) > 0)

class TestHelpers(unittest.TestCase):

    def test_date_validation(self):
        self.assertTrue(is_valid_date(date.today()))
        self.assertFalse(is_valid_date(date(1900, 1, 1)))
        self.assertFalse(is_valid_date("not a date"))

    def test_price_validation(self):
        self.assertTrue(is_valid_price(10.5))
        self.assertTrue(is_valid_price(0))
        self.assertFalse(is_valid_price(-1))
        self.assertFalse(is_valid_price("abc"))

    def test_note_validation(self):
        self.assertTrue(is_valid_note("Great quarter!"))
        self.assertFalse(is_valid_note(""))
        self.assertFalse(is_valid_note("a" * 501))

    def test_holding_validation(self):
        h = {
            "date": date.today(),
            "price": 150.0,
            "note": "bullish",
            "shares": 10,
            "cost": 1500.0,
        }
        self.assertTrue(is_valid_holding(h))
        h_bad = dict(h, shares=-1)
        self.assertFalse(is_valid_holding(h_bad))

if __name__ == "__main__":
    unittest.main()
