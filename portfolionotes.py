# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: PortfolioNotes
import json, datetime

class PortfolioNotes:
    def __init__(self):
        self.holdings = {}
        self.notes = []
        self.snapshots = []
        self.reminders = []

    def add_holding(self, ticker, name, shares, cost_per_share):
        self.holdings[ticker] = {"name": name, "shares": shares, "cost_per_share": cost_per_share}

    def add_note(self, ticker, note, date=None):
        if date is None: date = datetime.date.today().isoformat()
        self.notes.append({"ticker": ticker, "note": note, "date": date})

    def add_snapshot(self, ticker, price, date=None):
        if date is None: date = datetime.date.today().isoformat()
        self.snapshots.append({"ticker": ticker, "price": price, "date": date})

    def add_reminder(self, ticker, message, date=None):
        if date is None: date = datetime.date.today().isoformat()
        self.reminders.append({"ticker": ticker, "message": message, "date": date})

pn = PortfolioNotes()
pn.add_holding("AAPL", "Apple Inc.", 10, 150.0)
pn.add_holding("MSFT", "Microsoft Corp.", 5, 280.0)
pn.add_note("AAPL", "Watching for Q4 earnings")
pn.add_snapshot("AAPL", 152.3, "2025-06-01")
pn.add_reminder("MSFT", "Check quarterly update", "2025-07-15")

with open("portfolio_notes.json", "w") as f:
    json.dump({
        "holdings": pn.holdings,
        "notes": pn.notes,
        "snapshots": pn.snapshots,
        "reminders": pn.reminders
    }, f, indent=2)
