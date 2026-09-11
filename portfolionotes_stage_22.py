# === Stage 22: Add favorite records and quick favorite listing ===
# Project: PortfolioNotes
class Favorite:
    def __init__(self, symbol, note=""):
        self.symbol = symbol
        self.note = note

    def to_dict(self):
        return {"symbol": self.symbol, "note": self.note}

    @classmethod
    def from_dict(cls, d):
        return cls(symbol=d["symbol"], note=d.get("note", ""))

    def __repr__(self):
        return f"Favorite({self.symbol}, {self.note!r})"


class FavoriteBook:
    def __init__(self):
        self._favorites = []

    def add(self, symbol, note=""):
        self._favorites.append(Favorite(symbol, note))

    def remove(self, symbol):
        self._favorites = [f for f in self._favorites if f.symbol != symbol]

    def get(self, symbol):
        for f in self._favorites:
            if f.symbol == symbol:
                return f
        return None

    def list_all(self):
        return list(self._favorites)

    def load(self, path):
        import json
        with open(path) as f:
            data = json.load(f)
        for d in data:
            self._favorites.append(Favorite.from_dict(d))

    def save(self, path):
        import json
        with open(path, "w") as f:
            json.dump([fav.to_dict() for fav in self._favorites], f, indent=2)
