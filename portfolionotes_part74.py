# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: PortfolioNotes
def compare_snapshots(snapshots, metric):
    """Compare a numeric price metric between two snapshots."""
    if not isinstance(snapshots, list) or len(snapshots) < 2:
        return None
    before = snapshots[0][metric]
    after = snapshots[-1][metric]
    if before == 0:
        return None
    return (after - before) / before * 100.0
