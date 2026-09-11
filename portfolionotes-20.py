# === Stage 20: Add duplicate detection for newly created records ===
# Project: PortfolioNotes
def _check_duplicates(self, record):
    if not self._records:
        return
    for other in self._records:
        if record.id == other.id:
            return
        if (record.holding_symbol == other.holding_symbol and
            record.date == other.date):
            self._records.remove(other)
            return
    self._records.append(record)
