# === Stage 66: Add export of a short status dashboard ===
# Project: PortfolioNotes
def export_status_dashboard(path="status_dashboard.txt"):
    if not os.path.exists(DATA_FILE):
        return
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return
    holdings = data.get("holdings", [])
    notes = data.get("notes", [])
    snapshots = data.get("snapshots", [])
    reminders = data.get("reminders", [])
    now = datetime.datetime.now()
    lines = []
    lines.append("PortfolioNotes Status Dashboard")
    lines.append("=" * 30)
    lines.append("Generated: " + now.strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("Total Holdings: " + str(len(holdings)))
    total_cost = sum(float(h.get("cost", 0)) for h in holdings)
    lines.append("Total Cost: " + str(round(total_cost, 2)))
    lines.append("")
    for h in holdings:
        name = h.get("name", "Unknown")
        qty = h.get("qty", 0)
        cost = float(h.get("cost", 0))
        lines.append("Holding: " + name + " (Qty: " + str(qty) + ", Cost: " + str(round(cost, 2)) + ")")
    lines.append("")
    lines.append("Recent Price Snapshots (last 5):")
    recent = sorted(snapshots, key=lambda s: s.get("timestamp", ""), reverse=True)[:5]
    for s in recent:
        lines.append("  " + s.get("name", "Unknown") + " - " + str(s.get("price", 0)) + " (" + s.get("timestamp", "") + ")")
    lines.append("")
    lines.append("Active Reminders (next 7 days):")
    soon = [r for r in reminders if datetime.datetime.fromisoformat(r.get("due", now.isoformat())) - now <= datetime.timedelta(days=7)]
    for r in soon:
        lines.append("  " + r.get("message", "") + " (Due: " + r.get("due", "") + ")")
    lines.append("")
    lines.append("Total Notes: " + str(len(notes)))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
