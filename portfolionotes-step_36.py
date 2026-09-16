# === Stage 36: Add templates for quickly creating common records ===
# Project: PortfolioNotes
# Templates for quickly creating common records
TEMPLATE_HOLDING = """
{
    "symbol": "{symbol}",
    "name": "{name}",
    "quantity": {quantity},
    "avg_cost": {avg_cost},
    "note": ""
}
"""

TEMPLATE_NOTE = """
{
    "date": "{date}",
    "content": "{content}",
    "tags": []
}
"""

TEMPLATE_PRICE_SNAPSHOT = """
{
    "symbol": "{symbol}",
    "date": "{date}",
    "price": {price},
    "change_pct": {change_pct}
}
"""

TEMPLATE_REMINDER = """
{
    "title": "{title}",
    "description": "{description}",
    "date": "{date}",
    "time": "{time}",
    "recurring": {recurring}
}
"""
