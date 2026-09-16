# === Stage 35: Add active user switching and user-specific records ===
# Project: PortfolioNotes
class UserStore:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        self.users[user_id] = {"name": name, "notes": {}}

    def get_user(self, user_id):
        return self.users.get(user_id)

    def set_note(self, user_id, ticker, note, date):
        if user_id not in self.users:
            raise ValueError("User not found")
        self.users[user_id]["notes"][ticker] = {"note": note, "date": date}

    def get_note(self, user_id, ticker):
        user = self.users.get(user_id)
        if not user:
            return None
        return user["notes"].get(ticker)

    def get_all_notes(self, user_id):
        user = self.users.get(user_id)
        if not user:
            return {}
        return user["notes"]

    def delete_note(self, user_id, ticker):
        user = self.users.get(user_id)
        if not user or ticker not in user["notes"]:
            return False
        del user["notes"][ticker]
        return True
