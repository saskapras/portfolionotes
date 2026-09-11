# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: PortfolioNotes
def add_tag(self, note_id, tag):
    """Attach a tag to a note."""
    if note_id not in self.notes:
        raise KeyError(f"Note {note_id} not found")
    if tag not in self.tags:
        self.tags[tag] = set()
    self.tags[tag].add(note_id)
    self.notes[note_id]['tags'].add(tag)

def remove_tag(self, note_id, tag):
    """Detach a tag from a note."""
    if tag not in self.tags or note_id not in self.tags[tag]:
        raise KeyError(f"Tag {tag} not attached to note {note_id}")
    self.tags[tag].discard(note_id)
    if not self.tags[tag]:
        del self.tags[tag]
    self.notes[note_id]['tags'].discard(tag)

def summarize_by_tag(self, tag):
    """Return a dict of tag -> list of note titles."""
    if tag not in self.tags:
        return {}
    return {tag: [self.notes[nid]['title'] for nid in self.tags[tag]]}
