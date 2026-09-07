# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: PortfolioNotes
def search_notes(self, query, case_sensitive=False):
    """Search notes across title, body, and tags with optional case sensitivity."""
    if not case_sensitive:
        query = query.lower()
        title_lower = [note.get('title', '').lower() for note in self.notes]
        body_lower = [note.get('body', '').lower() for note in self.notes]
        tags_lower = [note.get('tags', []) for note in self.notes]
    else:
        title_lower = [note.get('title', '') for note in self.notes]
        body_lower = [note.get('body', '') for note in self.notes]
        tags_lower = [note.get('tags', []) for note in self.notes]

    results = []
    for i, note in enumerate(self.notes):
        if query in title_lower[i] or query in body_lower[i]:
            results.append(note)
            continue
        if query in ' '.join(tags_lower[i]):
            results.append(note)

    return results
