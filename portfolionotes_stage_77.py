# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: PortfolioNotes
def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def parse_float(value: str) -> float:
    return float(value)


def parse_int(value: str) -> int:
    return int(value)


def today_str() -> str:
    return datetime.date.today().isoformat()


def default_notes() -> dict:
    return {}


def default_snapshots() -> dict:
    return {}


def default_reminders() -> list:
    return []


def find_by_symbol(holdings: list, symbol: str) -> dict:
    for holding in holdings:
        if holding.get("symbol") == symbol:
            return holding
    return {}


def format_money(amount: float) -> str:
    return f"${amount:,.2f}"


def format_percent(change: float) -> str:
    return f"{change:+.2f}%"


def filter_due_reminders(reminders: list, now: datetime.datetime) -> list:
    return [r for r in reminders if r.get("due") <= now.isoformat()]


def add_note(holdings: list, symbol: str, text: str) -> list:
    holding = find_by_symbol(holdings, symbol)
    if holding:
        notes = holding.setdefault("notes", {})
        notes[symbol] = text
    return holdings


def snapshot_price(holdings: list, symbol: str, price: float) -> list:
    holding = find_by_symbol(holdings, symbol)
    if holding:
        snapshots = holding.setdefault("snapshots", {})
        snapshots[today_str()] = price
    return holdings
