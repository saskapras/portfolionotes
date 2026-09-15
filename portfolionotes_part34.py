# === Stage 34: Add support for multiple local user profiles ===
# Project: PortfolioNotes
import json
from pathlib import Path
from datetime import datetime

class UserProfiles:
    def __init__(self, profiles_path: str = "profiles.json"):
        self.profiles_path = Path(profiles_path)
        self.profiles = {}
        self._load()

    def _load(self):
        if self.profiles_path.exists():
            with open(self.profiles_path, "r") as f:
                self.profiles = json.load(f)
        else:
            self.profiles = {}

    def get_profile(self, name: str) -> dict:
        return self.profiles.get(name, {"name": name, "notes": {}, "reminders": []})

    def save(self):
        with open(self.profiles_path, "w") as f:
            json.dump(self.profiles, f, indent=2)

    def add_profile(self, name: str, notes: dict = None, reminders: list = None):
        self.profiles[name] = {
            "name": name,
            "notes": notes or {},
            "reminders": reminders or [],
        }
        self.save()
