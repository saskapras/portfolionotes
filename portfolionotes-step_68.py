# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: PortfolioNotes
def show_changelog(log, days=90):
    """Print a compact changelog derived from the activity log."""
    cutoff = (datetime.now() - timedelta(days=days)).date()
    lines = []
    for entry in reversed(log):
        if entry.get("date") and entry["date"] >= cutoff:
            lines.append(f"{entry['date']} — {entry.get('message', '')}")
    if lines:
        print("Changelog (last {} days)".format(days))
        print("\n".join(lines))
    else:
        print("No activity in the last {} days.".format(days))
