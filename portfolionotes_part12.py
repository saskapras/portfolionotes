# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: PortfolioNotes
import json

def load_notes(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"Note data is malformed: {e}")
        return []
    except PermissionError:
        print("Cannot read file: permission denied")
        return []
