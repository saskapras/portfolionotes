# === Stage 67: Add a function that returns key project metrics ===
# Project: PortfolioNotes
def get_project_metrics(holdings, notes, snapshots, reminders):
    total_holdings = len(holdings)
    total_notes = len(notes)
    total_snapshots = sum(len(snapshots.get(h, [])) for h in holdings)
    total_reminders = len(reminders)
    active_notes = sum(1 for n in notes if n.get("active", True))
    due_reminders = sum(1 for r in reminders if r.get("due") and r["due"] <= date.today())
    return {
        "total_holdings": total_holdings,
        "total_notes": total_notes,
        "active_notes": active_notes,
        "total_snapshots": total_snapshots,
        "total_reminders": total_reminders,
        "due_reminders": due_reminders,
    }
