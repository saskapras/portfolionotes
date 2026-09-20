# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: PortfolioNotes
import json

# --- PortfolioNotes demo scenario ---
portfolio = {
    "holdings": [
        {"symbol": "AAPL", "shares": 10, "cost_basis": 150.0},
        {"symbol": "GOOGL", "shares": 5,  "cost_basis": 2800.0},
    ],
    "notes": {
        "AAPL": "Consider trimming if it breaks above $200.",
        "GOOGL": "Hold for the AI push; stop-loss at $2500.",
    },
    "price_snapshots": [
        {"symbol": "AAPL", "date": "2024-06-10", "price": 187.50},
        {"symbol": "AAPL", "date": "2024-06-17", "price": 192.30},
        {"symbol": "GOOGL", "date": "2024-06-10", "price": 2750.00},
    ],
    "reminders": [
        {"symbol": "AAPL", "date": "2024-06-24", "message": "Review AAPL earnings impact."},
        {"symbol": "GOOGL", "date": "2024-06-28", "message": "Rebalance if price crosses $2600."},
    ],
}

print("=== PortfolioNotes Demo ===")
print(f"Holdings: {len(portfolio['holdings'])} positions")
for h in portfolio['holdings']:
    print(f"  {h['symbol']}: {h['shares']} shares @ ${h['cost_basis']:.2f}")

print(f"Notes: {len(portfolio['notes'])} entries")
for sym, note in portfolio['notes'].items():
    print(f"  {sym}: {note}")

print(f"Price snapshots: {len(portfolio['price_snapshots'])} records")
for ps in portfolio['price_snapshots']:
    print(f"  {ps['symbol']} on {ps['date']}: ${ps['price']:.2f}")

print(f"Reminders: {len(portfolio['reminders'])} alerts")
for r in portfolio['reminders']:
    print(f"  {r['symbol']} on {r['date']}: {r['message']}")

# --- Persist to disk (optional) ---
with open("portfolio_notes.json", "w") as f:
    json.dump(portfolio, f, indent=2)
print("\nSaved portfolio_notes.json")
