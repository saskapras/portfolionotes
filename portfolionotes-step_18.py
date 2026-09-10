# === Stage 18: Add an activity log with timestamps and action names ===
# Project: PortfolioNotes
import datetime

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, details=None):
        entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'action': action,
            'details': details or ''
        }
        self.entries.append(entry)
        return entry

    def get_log(self):
        return self.entries[-10:]
