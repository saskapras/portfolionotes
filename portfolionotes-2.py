# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: PortfolioNotes
@dataclass
class Holding:
    symbol: str
    name: str
    quantity: Decimal
    avg_cost: Decimal
    current_price: Decimal

@dataclass
class Note:
    title: str
    body: str
    created_at: datetime
    updated_at: datetime

@dataclass
class PriceSnapshot:
    symbol: str
    price: Decimal
    date: datetime

@dataclass
class Reminder:
    title: str
    message: str
    due_date: datetime
    is_active: bool
