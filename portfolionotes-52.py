# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: PortfolioNotes
def get_holdings_summary(holdings: list) -> dict:
    """Return a summary of all holdings, including total cost basis and average price."""
    total_cost = sum(h.get("cost", 0) for h in holdings)
    total_shares = sum(h.get("shares", 0) for h in holdings)
    avg_price = total_cost / total_shares if total_shares else 0
    return {
        "total_cost": total_cost,
        "total_shares": total_shares,
        "average_price": avg_price,
        "count": len(holdings),
    }

def get_notes_by_date(notes: list, target_date: str) -> list:
    """Return notes added on the given date (YYYY-MM-DD)."""
    return [n for n in notes if n.get("date") == target_date]

def get_price_snapshots_for_stock(snapshots: list, symbol: str) -> list:
    """Return all price snapshots for a specific stock symbol."""
    return [s for s in snapshots if s.get("symbol") == symbol]

def get_reminders_due_in_days(reminders: list, days: int) -> list:
    """Return reminders that are due within the specified number of days."""
    from datetime import datetime, timedelta
    today = datetime.now().date()
    target_date = today + timedelta(days=days)
    return [r for r in reminders if r.get("date") <= target_date]
