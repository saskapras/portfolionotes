# === Stage 89: Add final consistency checks for names, statuses, and dates ===
# Project: PortfolioNotes
def check_portfolio_consistency(holdings, notes, snapshots, reminders):
    errors = []
    for h in holdings:
        if not h['name']:
            errors.append(f"holding missing name: {h}")
        if h.get('status') not in ('active', 'closed', 'watching'):
            errors.append(f"invalid status {h.get('status')!r} for {h['name']}")
        if h.get('buy_date') and h['buy_date'] > h.get('sell_date', ''):
            errors.append(f"buy_date after sell_date for {h['name']}")
    for n in notes:
        if not n['name']:
            errors.append(f"note missing name: {n}")
        if not n['body'] or not isinstance(n['body'], str):
            errors.append(f"note body invalid for {n['name']}")
    for s in snapshots:
        if not s['name']:
            errors.append(f"snapshot missing name: {s}")
        if not isinstance(s['price'], (int, float)):
            errors.append(f"snapshot price invalid for {s['name']}")
        if s.get('date') and s['date'] > s.get('date', ''):
            errors.append(f"snapshot date malformed for {s['name']}")
    for r in reminders:
        if not r['name']:
            errors.append(f"reminder missing name: {r}")
        if not isinstance(r['when'], (int, float)):
            errors.append(f"reminder when invalid for {r['name']}")
    return errors
