# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: PortfolioNotes
def seed_demo_data(db, user_id=None):
    user_id = user_id or db.get_default_user_id()
    holdings = [
        ("AAPL", "Apple Inc.", 42.5, 185.10),
        ("MSFT", "Microsoft Corp.", 30.0, 412.75),
        ("BTC", "Bitcoin", 1.2, 64230.0),
    ]
    for symbol, name, qty, cost in holdings:
        db.add_holding(user_id, symbol, name, qty, cost)
    db.add_price_snapshot(user_id, "AAPL", "2024-01-02", 182.5)
    db.add_price_snapshot(user_id, "AAPL", "2024-01-03", 188.9)
    db.add_price_snapshot(user_id, "MSFT", "2024-01-02", 410.0)
    db.add_note(user_id, "AAPL", "Hold for long term dividend growth.", "2024-01-01")
    db.add_reminder(user_id, "Review AAPL position", "2024-01-10", "2024-01-05")
