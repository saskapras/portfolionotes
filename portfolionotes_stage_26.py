# === Stage 26: Add weekly summary calculations ===
# Project: PortfolioNotes
def weekly_summary(holdings, notes, snapshots):
    """Compute a compact weekly summary for the portfolio."""
    if not snapshots:
        return {"period": "N/A", "total_return": 0.0, "top_holder": None}
    sorted_snap = sorted(snapshots, key=lambda s: s["date"])
    start, end = sorted_snap[0], sorted_snap[-1]
    start_date = start["date"].date()
    end_date = end["date"].date()
    delta_days = (end_date - start_date).days
    if delta_days == 0:
        delta_days = 1
    portfolio_start = sum(h["quantity"] * h["price"] for h in holdings)
    portfolio_end = sum(h["quantity"] * s["price"] for h in holdings for s in snapshots if s["date"].date() == end_date)
    if portfolio_start == 0:
        return {"period": f"{start_date} to {end_date}", "total_return": 0.0, "top_holder": None}
    total_return = (portfolio_end - portfolio_start) / portfolio_start * 100
    weekly_return = portfolio_end / portfolio_start ** (1 / delta_days) ** 100 - 100
    top_holder = max(holdings, key=lambda h: h["quantity"] * end_date.weekday())
    return {
        "period": f"{start_date} to {end_date}",
        "total_return": total_return,
        "weekly_return": weekly_return,
        "top_holder": top_holder["symbol"] if top_holder else None,
    }
