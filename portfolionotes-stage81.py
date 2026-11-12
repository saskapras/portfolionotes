# === Stage 81: Add final README text as a module string with usage examples ===
# Project: PortfolioNotes
NOTES = """
PortfolioNotes — a simple investment note tracker.

Track your holdings, attach notes, capture price snapshots, and set
reminders — all in plain text, no dependencies, no database.

Quick start
-----------
Run the demo to explore the full workflow:

    python portfolio_notes.py

Or import the modules directly:

    from portfolio_notes import Portfolio, Note, PriceSnapshot

    portfolio = Portfolio()
    portfolio.add_holding("AAPL", 50)
    note = Note("Buy below $180", "Positive momentum")
    portfolio.add_note(note)
    snapshot = PriceSnapshot("AAPL", 185.50, datetime.date(2025, 1, 1))
    portfolio.record_snapshot(snapshot)
    portfolio.save("portfolio.txt")

Commands (run from the project directory)
-----------------------------------------
    python portfolio_notes.py add_holding AAPL 50
    python portfolio_notes.py add_note "Buy below 180" "Positive momentum"
    python portfolio_notes.py snapshot AAPL 185.50 2025-01-01
    python portfolio_notes.py reminder AAPL 180 2025-01-10
    python portfolio_notes.py show
    python portfolio_notes.py list_notes
    python portfolio_notes.py snapshots
    python portfolio_notes.py reminders
    python portfolio_notes.py remove AAPL
    python portfolio_notes.py delete_note 1
    python portfolio_notes.py save portfolio.txt
    python portfolio_notes.py load portfolio.txt

Data model
----------
Each holding may have several notes, price snapshots, and reminders.
Notes are free text; snapshots are date-stamped prices; reminders are
date-stamped price thresholds. Everything is stored as plain text so the
project stays dependency-free and easy to read.
"""
