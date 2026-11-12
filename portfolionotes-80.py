# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: PortfolioNotes
def format_holding(hold):
    name = hold["name"]
    qty = hold["qty"]
    price = hold.get("price")
    if price is None:
        value = f"{qty} {name}"
    else:
        value = f"{qty} {name} @ {price:.2f}"
    note = hold.get("note", "").strip()
    if note:
        value += f" — {note}"
    return value


def format_snapshot(snap):
    date = snap.get("date", "")
    price = snap.get("price")
    if price is None:
        return f"{date}"
    return f"{date} @ {price:.2f}"


def format_reminder(rem):
    text = rem.get("text", "").strip()
    when = rem.get("when", "")
    if not when:
        return f"Reminder: {text}"
    return f"Reminder ({when}): {text}"


def format_portfolio(portfolio):
    lines = []
    for hold in portfolio["holdings"]:
        lines.append(format_holding(hold))
    for snap in portfolio["snapshots"]:
        lines.append("  " + format_snapshot(snap))
    for rem in portfolio["reminders"]:
        lines.append(format_reminder(rem))
    return "\n".join(lines)
