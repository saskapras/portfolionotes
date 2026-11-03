# === Stage 63: Add relationships between records where useful ===
# Project: PortfolioNotes
class Holding:
    def __init__(self, ticker, quantity, avg_cost, notes=""):
        self.ticker = ticker
        self.quantity = quantity
        self.avg_cost = avg_cost
        self.notes = notes

    def link_note(self, note_id):
        if note_id not in self.notes:
            self.notes.append(note_id)

    def linked_notes(self):
        return [n for n in self.notes if n.exists]


class Note:
    def __init__(self, title, body, holding=None, price_snapshot=None):
        self.id = None
        self.title = title
        self.body = body
        self.holding = holding
        self.price_snapshot = price_snapshot

    def belongs_to(self, holding):
        return holding is not None and holding.ticker == self.ticker


class PriceSnapshot:
    def __init__(self, holding, price, date):
        self.id = None
        self.holding = holding
        self.price = price
        self.date = date

    def is_for(self, holding):
        return holding is not None and holding.ticker == self.ticker
