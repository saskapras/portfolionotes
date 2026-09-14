# === Stage 32: Add pagination helpers for long console output ===
# Project: PortfolioNotes
def paginate(text, width=80):
    """Yield text wrapped to `width` characters for long console output."""
    for i in range(0, len(text), width):
        yield text[i:i + width]
