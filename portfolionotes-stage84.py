# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: PortfolioNotes
def purge_duplicate_notes():
    seen = {}
    for note_id, content in NOTES.items():
        key = content.strip().lower()
        if key in seen:
            del NOTES[note_id]
        else:
            seen[key] = note_id


def normalize_price(value):
    if isinstance(value, str):
        value = value.replace(',', '').strip()
    return float(value)


def snapshot_price(symbol, price):
    key = symbol.upper()
    if key not in PRICE_SNAPSHOTS:
        PRICE_SNAPSHOTS[key] = []
    PRICE_SNAPSHOTS[key].append(normalize_price(price))


def find_due_reminders(today=None):
    today = today or date.today()
    due = []
    for reminder_id, reminder in REMINDERS.items():
        if reminder['due'] <= today and reminder_id not in [r['id'] for r in due]:
            due.append(reminder)
    return due
