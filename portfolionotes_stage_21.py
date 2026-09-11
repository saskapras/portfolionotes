# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: PortfolioNotes
def archive_record(record):
    return {**record, "archived": True, "archived_at": datetime.now().isoformat()}

def restore_record(record):
    return {**record, "archived": False}

def process_records(records):
    return [archive_record(r) for r in records if not r.get("archived")]
