# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: PortfolioNotes
import re
from datetime import datetime

DATE_FORMATS = [
    ("%Y-%m-%d", "YYYY-MM-DD"),
    ("%Y/%m/%d", "YYYY/MM/DD"),
    ("%m-%d-%Y", "MM-DD-YYYY"),
    ("%m/%d/%Y", "MM/DD/YYYY"),
    ("%d-%m-%Y", "DD-MM-YYYY"),
    ("%d/%m/%Y", "DD/MM/YYYY"),
    ("%Y%m%d", "YYYYMMDD"),
]

def parse_date(date_str: str) -> datetime:
    """Parse a date string using common formats and return a datetime object.

    Raises ValueError with a clear message listing the formats tried.
    """
    date_str = date_str.strip()
    if not date_str:
        raise ValueError("Empty date string provided.")
    for fmt, label in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(
        f"Unable to parse date: '{date_str}'. Tried formats: {', '.join(f'({f}){l}' for f, l in DATE_FORMATS)}"
    )
