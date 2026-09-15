# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: PortfolioNotes
def get_settings():
    return {
        "currency": "USD",
        "price_alert_thresholds": [],
        "reminder_enabled": False,
        "reminder_time": "08:00",
        "reminder_days": ["mon", "tue", "wed", "thu", "fri"],
        "note_retention_days": 365,
        "auto_save": True,
        "theme": "light",
    }

def update_settings(settings, updates=None):
    if updates is None:
        return settings
    return {**settings, **updates}

def validate_setting_name(name):
    return name in get_settings()

def validate_setting_value(name, value):
    if name == "currency":
        return value in ("USD", "EUR", "GBP", "JPY", "CNY")
    if name == "theme":
        return value in ("light", "dark", "auto")
    if name == "reminder_time":
        try:
            int(value.split(":")[0])
            int(value.split(":")[1])
            return True
        except:
            return False
    if name == "note_retention_days":
        return isinstance(value, int) and value > 0
    if name == "reminder_days":
        return all(d in ("mon", "tue", "wed", "thu", "fri", "sat", "sun") for d in value)
    return True
