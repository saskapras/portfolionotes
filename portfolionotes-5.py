# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: PortfolioNotes
def update_holding(self, holding_id, **kwargs):
    """Update fields of an existing holding; missing fields are left unchanged."""
    rec = self._get_record(holding_id)
    if rec is None:
        raise KeyError(f"Holding {holding_id!r} not found")
    for field, value in kwargs.items():
        if not field.startswith("_"):
            setattr(rec, field, value)
    self._save()
    return rec
