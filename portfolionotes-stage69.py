# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: PortfolioNotes
def reset_demo_data(db_path='portfolio.db'):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS holdings')
    cur.execute('DROP TABLE IF EXISTS notes')
    cur.execute('DROP TABLE IF EXISTS price_snapshots')
    cur.execute('DROP TABLE IF EXISTS reminders')
    demo = [
        ('AAPL', 'Apple Inc.', 185.50, 'Strong services growth'),
        ('MSFT', 'Microsoft Corp.', 412.30, 'Cloud momentum solid'),
        ('GOOGL', 'Alphabet Inc.', 172.10, 'AI ads uplift'),
        ('TSLA', 'Tesla Inc.', 245.60, 'Watch delivery numbers'),
    ]
    cur.executemany('INSERT INTO holdings (ticker, name, price, note) VALUES (?,?,?,?)', demo)
    snapshots = [
        ('AAPL', '2024-01-01', 180.20),
        ('AAPL', '2024-01-15', 185.50),
        ('MSFT', '2024-01-01', 400.10),
        ('MSFT', '2024-01-15', 412.30),
    ]
    cur.executemany('INSERT INTO price_snapshots (ticker, date, price) VALUES (?,?,?)', snapshots)
    reminders = [
        ('AAPL', '2024-02-01', 'Reassess position'),
        ('TSLA', '2024-02-10', 'Review delivery report'),
    ]
    cur.executemany('INSERT INTO reminders (ticker, date, message) VALUES (?,?,?)', reminders)
    conn.commit()
    conn.close()
    print('Demo data reset complete.')
