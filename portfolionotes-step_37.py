# === Stage 37: Add recommendations for the next useful action ===
# Project: PortfolioNotes
import json
from datetime import datetime

class ReminderManager:
    def __init__(self, notes_file="portfolio_notes.json"):
        with open(notes_file, "r") as f:
            self.notes = json.load(f)

    def add_reminder(self, symbol, message, days_from_now=7):
        deadline = (datetime.now() + timedelta(days=days_from_now)).strftime("%Y-%m-%d")
        reminder = {
            "symbol": symbol,
            "message": message,
            "deadline": deadline,
            "added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes["reminders"].append(reminder)
        with open(notes_file, "w") as f:
            json.dump(self.notes, f, indent=2)
        return reminder

    def get_upcoming_reminders(self, days_ahead=30):
        today = datetime.now()
        upcoming = []
        for r in self.notes["reminders"]:
            deadline = datetime.strptime(r["deadline"], "%Y-%m-%d")
            if (deadline - today).days <= days_ahead:
                upcoming.append(r)
        return upcoming

    def remove_reminder(self, reminder_id):
        self.notes["reminders"] = [r for r in self.notes["reminders"] if r.get("id") != reminder_id]
        with open(notes_file, "w") as f:
            json.dump(self.notes, f, indent=2)
