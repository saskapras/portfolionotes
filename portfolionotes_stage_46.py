# === Stage 46: Add a schema version field and migration helper ===
# Project: PortfolioNotes
SCHEMA_VERSION = 3

def migrate_to_v3(db_path):
    """Upgrade schema: add schema_version column if missing."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    try:
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='holdings'")
        if c.fetchone() is None:
            return
        c.execute("PRAGMA table_info(holdings)")
        cols = {row[1] for row in c.fetchall()}
        if "schema_version" not in cols:
            c.execute("ALTER TABLE holdings ADD COLUMN schema_version INTEGER DEFAULT 3")
            conn.commit()
            print(f"Schema migrated to v{SCHEMA_VERSION}.")
        else:
            print("Already at v3 schema.")
    finally:
        conn.close()
