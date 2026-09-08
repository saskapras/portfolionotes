# === Stage 11: Add JSON export for the current application state ===
# Project: PortfolioNotes
def export_state(state, filename="portfolio_notes.json"):
    """Export the current application state as a compact JSON file."""
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, sort_keys=True)
    print(f"State exported to {filename}")
