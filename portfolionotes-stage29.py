# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: PortfolioNotes
def upcoming_reminders(reminders, days_ahead=30):
    """Return reminder items sorted by date, only those within `days_ahead` days."""
    today = datetime.date.today()
    cutoff = today + timedelta(days=days_ahead)
    return [r for r in reminders if today <= r["date"] <= cutoff], reminders
