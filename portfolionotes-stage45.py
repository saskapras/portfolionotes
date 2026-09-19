# === Stage 45: Add restore from backup with validation ===
# Project: PortfolioNotes
def restore_from_backup(backup_path, validation=True):
    """Restore portfolio data from a JSON backup file with optional validation."""
    import json
    if not validation:
        with open(backup_path, 'r') as f:
            return json.load(f)
    try:
        with open(backup_path, 'r') as f:
            data = json.load(f)
        required_keys = ['holdings', 'notes', 'snapshots', 'reminders']
        for key in required_keys:
            assert key in data, f"Missing required key: {key}"
        assert isinstance(data['holdings'], list)
        assert isinstance(data['notes'], list)
        assert isinstance(data['snapshots'], list)
        assert isinstance(data['reminders'], list)
        return data
    except (json.JSONDecodeError, FileNotFoundError, AssertionError) as e:
        raise ValueError(f"Invalid backup file: {e}")
