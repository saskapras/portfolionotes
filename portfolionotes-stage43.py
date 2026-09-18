# === Stage 43: Add CSV import for the primary record type ===
# Project: PortfolioNotes
import csv
from datetime import date

def import_holdings(filename):
    """Import holdings from a CSV file with columns: name, symbol, quantity, cost_basis, purchase_date."""
    holdings = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            holdings.append({
                'name': row['name'],
                'symbol': row['symbol'],
                'quantity': float(row['quantity']),
                'cost_basis': float(row['cost_basis']),
                'purchase_date': row['purchase_date'],
            })
    return holdings
