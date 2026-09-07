# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: PortfolioNotes
def sort_notes(notes, key='title'):
    return sorted(notes, key=lambda n: n.get(key, ''))

def sort_notes_by_date(notes):
    return sorted(notes, key=lambda n: n.get('date', ''), reverse=True)

def sort_notes_by_priority(notes):
    return sorted(notes, key=lambda n: n.get('priority', 0), reverse=True)

def sort_notes_by_last_update(notes):
    return sorted(notes, key=lambda n: n.get('last_update', ''), reverse=True)
