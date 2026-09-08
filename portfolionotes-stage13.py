# === Stage 13: Add file save support using a configurable path ===
# Project: PortfolioNotes
import os
from pathlib import Path

DEFAULT_PATH = Path("portfolio_notes.json")

def save_notes(notes, path=DEFAULT_PATH):
    """Persist notes to JSON, creating parent dirs if needed."""
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "holdings": notes.get("holdings", {}),
        "notes": notes.get("notes", {}),
        "price_snapshots": notes.get("price_snapshots", {}),
        "reminders": notes.get("reminders", []),
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_notes(path=DEFAULT_PATH):
    """Return notes dict or empty structure if file missing."""
    if not path.exists():
        return {"holdings": {}, "notes": {}, "price_snapshots": {}, "reminders": []}
    with open(path) as f:
        return json.load(f)
