# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: PortfolioNotes
import re


REQUIRED_FIELDS = {"ticker", "company", "price"}
ID_PATTERN = re.compile(r"^[A-Z]{1,5}$")


def validate_required(fields, required):
    for f in required:
        if not fields.get(f):
            raise ValueError(f"Missing required field: {f}")


def validate_ticker(ticker):
    if not ID_PATTERN.match(ticker):
        raise ValueError(f"Invalid ticker format: {ticker}")


def validate_short_text(text, max_len=100):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Text must be a non-empty string")
    if len(text) > max_len:
        raise ValueError(f"Text exceeds {max_len} characters")


def validate_price(price):
    if price < 0:
        raise ValueError("Price must be non-negative")
    return round(float(price), 2)
