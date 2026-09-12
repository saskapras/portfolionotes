# === Stage 24: Add grouped summaries by category or status ===
# Project: PortfolioNotes
def grouped_summaries(records):
    groups = {}
    for r in records:
        key = r.get("category", r.get("status", "uncategorized"))
        groups.setdefault(key, []).append(r)
    summaries = []
    for key, items in groups.items():
        vals = [float(x.get("price", x.get("amount", 0))) for x in items if x.get("price") or x.get("amount")]
        total = sum(vals)
        summaries.append({"group": key, "count": len(items), "total": total})
    return summaries
