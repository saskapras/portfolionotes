# === Stage 41: Add plain text import for a simple line-based format ===
# Project: PortfolioNotes
def load_notes_from_txt(filepath):
    """Load notes from a plain text file with one note per line.

    Each line is expected to be in the format:
        YYYY-MM-DD|Stock|Price|Note

    Lines starting with '#' are treated as comments and ignored.
    """
    notes = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|')
            if len(parts) != 4:
                continue
            date_str, stock, price_str, note = parts
            try:
                price = float(price_str)
            except ValueError:
                continue
            notes.append({
                'date': date_str,
                'stock': stock,
                'price': price,
                'note': note,
            })
    return notes
