# === Stage 51: Add unit tests for search and filter behavior ===
# Project: PortfolioNotes
import pytest
from portfolio_notes.app import PortfolioNotes, Note, PriceSnapshot, Reminder


@pytest.fixture
def pn():
    pn = PortfolioNotes()
    pn.add_holding("AAPL", 100, 150.0)
    pn.add_holding("GOOGL", 50, 2800.0)
    pn.add_note("AAPL", "Strong buy signal")
    pn.add_note("GOOGL", "Watch for pullback")
    pn.add_snapshot("AAPL", 155.0)
    pn.add_snapshot("GOOGL", 2750.0)
    pn.add_reminder("AAPL", "2025-07-01", "Review AAPL")
    return pn


def test_search_by_symbol(pn):
    results = pn.search("AAPL")
    assert len(results) == 1
    assert results[0].symbol == "AAPL"


def test_search_by_partial_symbol(pn):
    results = pn.search("GOO")
    assert len(results) == 1
    assert results[0].symbol == "GOOGL"


def test_search_by_note_text(pn):
    results = pn.search("Strong buy")
    assert len(results) == 1
    assert results[0].type == "note"


def test_search_by_snapshot(pn):
    results = pn.search("155.0")
    assert len(results) == 1
    assert results[0].type == "snapshot"


def test_search_by_reminder(pn):
    results = pn.search("Review AAPL")
    assert len(results) == 1
    assert results[0].type == "reminder"


def test_filter_by_type(pn):
    notes = pn.filter("note")
    assert len(notes) == 2


def test_filter_by_type_no_match(pn):
    results = pn.filter("invalid")
    assert len(results) == 0


def test_filter_by_type_mixed(pn):
    results = pn.filter("note|snapshot")
    assert len(results) == 3


def test_search_empty_portfolio():
    pn = PortfolioNotes()
    assert len(pn.search("AAPL")) == 0
    assert len(pn.filter("note")) == 0
