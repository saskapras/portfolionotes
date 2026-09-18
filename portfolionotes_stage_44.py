# === Stage 44: Add backup creation for the data file ===
# Project: PortfolioNotes
def backup_data_file(source_path: str, backup_dir: str = ".") -> str:
    """Create a timestamped backup of the data file."""
    import os
    import shutil
    from datetime import datetime

    backup_dir = os.path.join(backup_dir, "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"portfolio_notes_backup_{timestamp}.json")
    shutil.copy2(source_path, backup_path)
    return backup_path
