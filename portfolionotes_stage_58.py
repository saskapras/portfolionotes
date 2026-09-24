# === Stage 58: Add bulk update behavior for selected records ===
# Project: PortfolioNotes
def bulk_update(self, records: list[dict]) -> list[dict]:
        """Update multiple records in one call. Each dict must contain at least
        the primary key (id) and the fields to change. Returns the updated
        records."""
        updated = []
        for rec in records:
            if not rec.get("id"):
                continue
            existing = self._get(rec["id"])
            if existing is None:
                continue
            existing.update(rec)
            self._save(existing)
            updated.append(existing)
        return updated
