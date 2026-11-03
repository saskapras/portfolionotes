# === Stage 64: Add validation for relationship references ===
# Project: PortfolioNotes
def validate_references():
    errors = []
    if "holdings" not in data:
        errors.append("missing 'holdings'")
        return errors
    holding_ids = {h["symbol"] for h in data["holdings"]}
    if "notes" not in data:
        return errors
    for note in data["notes"]:
        if note.get("holding_id") not in holding_ids:
            errors.append(f"note references unknown holding_id {note.get('holding_id')}")
        for snapshot in note.get("price_snapshots", []):
            if snapshot.get("holding_id") not in holding_ids:
                errors.append(f"price_snapshot references unknown holding_id {snapshot.get('holding_id')}")
        if note.get("reminder_id"):
            for reminder in data.get("reminders", []):
                if reminder.get("id") == note.get("reminder_id"):
                    break
            else:
                errors.append(f"note references unknown reminder_id {note.get('reminder_id')}")
    if "reminders" not in data:
        return errors
    for reminder in data["reminders"]:
        if reminder.get("holding_id") not in holding_ids:
            errors.append(f"reminder references unknown holding_id {reminder.get('holding_id')}")
    return errors
