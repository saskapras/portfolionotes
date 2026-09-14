# === Stage 28: Add overdue item detection based on due dates ===
# Project: PortfolioNotes
def detect_overdue_items(notes, today=None):
    if today is None:
        today = datetime.date.today()
    overdue = []
    for note in notes:
        if note.get("due_date") and note["due_date"] < today:
            overdue.append({
                "title": note["title"],
                "due_date": note["due_date"],
                "overdue_days": (today - note["due_date"]).days,
            })
    return overdue
