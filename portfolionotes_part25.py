# === Stage 25: Add daily summary calculations ===
# Project: PortfolioNotes
def daily_summary(holdings, price_snapshots):
    """Return a compact daily summary dict."""
    dates = sorted(set(h["date"] for h in price_snapshots))
    summary = {"dates": dates, "records": []}
    for d in dates:
        day = {"date": d, "holdings": [], "total_value": 0.0, "gain_pct": 0.0}
        for h in holdings:
            snap = next((s for s in price_snapshots if s["date"] == d and s["symbol"] == h["symbol"]), None)
            if snap:
                cost = h.get("cost_basis", 0)
                qty = h.get("quantity", 0)
                day["holdings"].append({"symbol": h["symbol"], "qty": qty})
                day["total_value"] += snap["price"] * qty
        if day["total_value"] > 0:
            day["gain_pct"] = ((day["total_value"] / 100.0) - 100)
        summary["records"].append(day)
    return summary
