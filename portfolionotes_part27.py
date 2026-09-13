# === Stage 27: Add monthly summary calculations ===
# Project: PortfolioNotes
def monthly_summary(prices):
    """Aggregate price snapshots by month and return a list of (year, month, avg_price) tuples."""
    grouped = {}
    for date, price in prices:
        key = (date.year, date.month)
        grouped.setdefault(key, []).append(price)
    return [(y, m, sum(vals) / len(vals)) for (y, m), vals in sorted(grouped.items())]
