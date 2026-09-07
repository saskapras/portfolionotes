# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: PortfolioNotes
def filter_notes(self, status=None, category=None, owner=None, tag=None):
    """Filter notes by status, category, owner, or tag.

    Args:
        status: 'active', 'completed', 'cancelled', or None for all.
        category: e.g., 'stocks', 'crypto', 'bonds', or None for all.
        owner: username string, or None for all.
        tag: tag string, or None for all.

    Returns:
        List of note dicts matching all provided filters.
    """
    results = list(self.notes.values())
    if status is not None:
        results = [n for n in results if n.get('status') == status]
    if category is not None:
        results = [n for n in results if n.get('category') == category]
    if owner is not None:
        results = [n for n in results if n.get('owner') == owner]
    if tag is not None:
        results = [n for n in results if tag in n.get('tags', [])]
    return results
