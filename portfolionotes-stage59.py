# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: PortfolioNotes
def delete_records(self, record_ids, confirmed=False):
    if not confirmed and record_ids:
        raise ValueError(
            "Bulk delete requires explicit confirmation. "
            "Call delete_records with confirmed=True."
        )
    ids_to_remove = set(record_ids)
    removed = []
    for rec in list(self._records.values()):
        if rec["id"] in ids_to_remove:
            removed.append(rec["id"])
            self._records.pop(rec["id"], None)
    return removed
