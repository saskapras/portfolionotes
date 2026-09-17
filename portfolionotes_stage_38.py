# === Stage 38: Add data integrity checks for broken references ===
# Project: PortfolioNotes
def check_references(data):
    """Validate that all cross-references within the portfolio data are intact.

    Checks:
    - Every note's 'symbol' exists in holdings.
    - Every price snapshot's 'symbol' exists in holdings.
    - Every reminder's 'symbol' exists in holdings.
    - Every holding's 'symbol' exists in price_snapshots.
    """
    if not isinstance(data, dict) or 'holdings' not in data:
        return False
    holdings = data['holdings']
    symbols = set(h['symbol'] for h in holdings) if isinstance(holdings, list) else set()
    issues = []
    for note in data.get('notes', []):
        sym = note.get('symbol')
        if sym and sym not in symbols:
            issues.append(f"Note '{note.get('id', '?')}' references unknown symbol '{sym}'")
    for snapshot in data.get('price_snapshots', []):
        sym = snapshot.get('symbol')
        if sym and sym not in symbols:
            issues.append(f"Snapshot '{snapshot.get('id', '?')}' references unknown symbol '{sym}'")
    for reminder in data.get('reminders', []):
        sym = reminder.get('symbol')
        if sym and sym not in symbols:
            issues.append(f"Reminder '{reminder.get('id', '?')}' references unknown symbol '{sym}'")
    if issues:
        return False, issues
    return True, []
