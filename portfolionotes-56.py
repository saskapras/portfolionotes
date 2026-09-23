# === Stage 56: Add compact error classes for domain failures ===
# Project: PortfolioNotes
class PortfolioError(Exception):
    """Base exception for PortfolioNotes domain errors."""
    pass


class HoldingNotFound(PortfolioError):
    """Raised when a holding id is not registered."""
    def __init__(self, holding_id: str):
        super().__init__(f"Holding not found: {holding_id}")
        self.holding_id = holding_id


class NoteConflict(PortfolioError):
    """Raised when updating a note for a holding that has no note yet."""
    def __init__(self, holding_id: str):
        super().__init__(f"Note conflict: no existing note for {holding_id}")
        self.holding_id = holding_id


class PriceSnapshotDuplicate(PortfolioError):
    """Raised when adding a snapshot with a duplicate (holding, date) pair."""
    def __init__(self, holding_id: str, date: str):
        super().__init__(f"Duplicate price snapshot for {holding_id} on {date}")
        self.holding_id = holding_id
        self.date = date


class ReminderMissed(PortfolioError):
    """Raised when a reminder deadline has passed without action."""
    def __init__(self, reminder_id: str, deadline: str):
        super().__init__(f"Missed reminder: {reminder_id} (deadline {deadline})")
        self.reminder_id = reminder_id
        self.deadline = deadline


class PortfolioStateError(PortfolioError):
    """Raised for invalid portfolio state transitions."""
    pass


class SnapshotStorageError(PortfolioError):
    """Raised when the price-snapshot storage cannot be read/written."""
    pass
