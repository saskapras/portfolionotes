# === Stage 83: Add regression tests for the final demo workflow ===
# Project: PortfolioNotes
def test_final_demo_workflow():
    from portfolio_notes import PortfolioNotes
    notes = PortfolioNotes()
    notes.add_holding("AAPL", price=150.0)
    notes.add_note("AAPL", "Long term hold")
    notes.add_snapshot("AAPL", 155.0)
    notes.add_reminder("AAPL", "Review quarterly")
    assert notes.lookup("AAPL") is not None
    assert notes.get_note("AAPL") == "Long term hold"
    assert notes.get_snapshot("AAPL") == 155.0
    assert notes.get_reminders("AAPL") == ["Review quarterly"]
