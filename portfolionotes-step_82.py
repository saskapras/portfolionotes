# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: PortfolioNotes
def demo(portfolio=None):
    portfolio = portfolio or Portfolio()
    holding = Holding("AAPL", "Apple Inc.", 120.5)
    note = Note("Strong buy, long-term hold", "Diversified tech giant")
    snapshot = PriceSnapshot("AAPL", 120.5, "2024-05-10")
    reminder = Reminder("Review AAPL position", "2024-06-01 09:00")

    portfolio.add_holding(holding)
    portfolio.add_note("AAPL", note)
    portfolio.add_snapshot(snapshot)
    portfolio.add_reminder(reminder)

    print("=== PortfolioNotes Demo ===")
    print(f"Holdings: {len(portfolio.holdings)}")
    for h in portfolio.holdings:
        print(f"  {h.symbol} - {h.name} @ ${h.price}")
    print(f"Notes for AAPL: {len(portfolio.notes_for('AAPL'))}")
    print(f"Snapshots: {len(portfolio.snapshots)}")
    print(f"Reminders: {len(portfolio.reminders)}")
    print("Demo complete.")
