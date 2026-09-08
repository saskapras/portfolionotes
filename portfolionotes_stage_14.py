# === Stage 14: Add file load support with fallback demo data ===
# Project: PortfolioNotes
def load_data():
    try:
        import json, os
        with open("notes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "holdings": [
                {"ticker": "AAPL", "shares": 10, "avg_cost": 150.0, "notes": "Long-term hold"},
                {"ticker": "MSFT", "shares": 5, "avg_cost": 300.0, "notes": "Watch for Q3 earnings"}
            ],
            "notes": [
                {"ticker": "AAPL", "date": "2024-01-15", "text": "Dropped below support level"},
                {"ticker": "MSFT", "date": "2024-02-01", "text": "Cloud revenue growing steadily"}
            ],
            "price_snapshots": [
                {"ticker": "AAPL", "date": "2024-01-15", "price": 148.5},
                {"ticker": "MSFT", "date": "2024-02-01", "price": 310.2}
            ],
            "reminders": [
                {"ticker": "AAPL", "note": "Review monthly", "next_date": "2024-03-15"}
            ]
        }
