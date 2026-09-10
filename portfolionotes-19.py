# === Stage 19: Add undo support for the last simple mutation ===
# Project: PortfolioNotes
class UndoableNote:
    def __init__(self, note_id, entry, previous_entry):
        self.note_id = note_id
        self.entry = entry
        self.previous_entry = previous_entry

    def undo(self):
        self.entry = self.previous_entry
