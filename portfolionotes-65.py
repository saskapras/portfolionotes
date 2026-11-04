# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: PortfolioNotes
def _load_holding(path):
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)

def _load_note(path):
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)

def _load_snapshot(path):
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)
