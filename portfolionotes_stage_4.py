# === Stage 4: Implement create operations for the primary records ===
# Project: PortfolioNotes
def add_holding(self, name, ticker, quantity, cost_price, note=None):
    """Add a new holding to the portfolio."""
    holding = {
        'name': name,
        'ticker': ticker,
        'quantity': quantity,
        'cost_price': cost_price,
        'note': note or '',
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    self.holdings.append(holding)
    return holding

def add_note(self, holding_name, content, reminder=None):
    """Add a note linked to a specific holding."""
    note = {
        'holding_name': holding_name,
        'content': content,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'reminder': reminder or None,
    }
    self.notes.append(note)
    return note

def add_price_snapshot(self, ticker, price, timestamp=None):
    """Record a price snapshot for a ticker."""
    if timestamp is None:
        timestamp = datetime.now()
    snapshot = {
        'ticker': ticker,
        'price': price,
        'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    self.price_snapshots.append(snapshot)
    return snapshot
