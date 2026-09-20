# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: PortfolioNotes
import unittest
from portfolio_notes.app import PortfolioNotes

class TestUpdateDelete(unittest.TestCase):

    def setUp(self):
        self.pn = PortfolioNotes()

    def test_update_nonexistent_holding_raises(self):
        with self.assertRaises(ValueError):
            self.pn.update_holding("missing", {"price": 10})

    def test_delete_nonexistent_holding_raises(self):
        with self.assertRaises(ValueError):
            self.pn.delete_holding("missing")

    def test_update_with_notes(self):
        self.pn.add_holding("AAPL", 10, 150, "good")
        self.pn.update_holding("AAPL", 11, 155)
        self.assertEqual(self.pn.holdings["AAPL"]["price"], 155)
        self.assertEqual(self.pn.holdings["AAPL"]["notes"], "good")

    def test_delete_then_add(self):
        self.pn.add_holding("MSFT", 20, 200)
        self.pn.delete_holding("MSFT")
        self.assertNotIn("MSFT", self.pn.holdings)
        self.pn.add_holding("MSFT", 20, 210)
        self.assertIn("MSFT", self.pn.holdings)
        self.assertEqual(self.pn.holdings["MSFT"]["shares"], 20)

    def test_update_preserves_original_notes(self):
        self.pn.add_holding("GOOGL", 5, 140, "buy dip")
        self.pn.update_holding("GOOGL", 6, 145)
        self.assertEqual(self.pn.holdings["GOOGL"]["notes"], "buy dip")

    def test_delete_all_holdings(self):
        self.pn.add_holding("A", 1, 1)
        self.pn.add_holding("B", 1, 2)
        self.pn.delete_holding("A")
        self.pn.delete_holding("B")
        self.assertEqual(self.pn.holdings, {})

if __name__ == "__main__":
    unittest.main()
