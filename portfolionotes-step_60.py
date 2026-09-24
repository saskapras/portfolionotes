# === Stage 60: Add saved views for frequently used filters ===
# Project: PortfolioNotes
class SavedView:
    def __init__(self, name, filters=None, columns=None):
        self.name = name
        self.filters = filters or {}
        self.columns = columns or None

    def apply_filters(self, records):
        result = []
        for r in records:
            match = True
            for key, val in self.filters.items():
                if r.get(key) != val:
                    match = False
                    break
            if match:
                result.append(r)
        return result

    def get_columns(self):
        return self.columns or list(self.filters.keys())
