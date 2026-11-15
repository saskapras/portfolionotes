# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: PortfolioNotes
def safe_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def safe_int(value, default=0):
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return default


def safe_str(value, default=""):
    if value is None:
        return default
    return str(value).strip()


def parse_bool(value, default=False):
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    return str(value).strip().lower() in ("1", "true", "yes", "y")


def normalize_number(text, default=0.0):
    if text is None:
        return default
    cleaned = str(text).replace(",", "").replace("$", "").strip()
    return safe_float(cleaned, default)


def safe_price(text, default=0.0):
    return normalize_number(text, default)


def safe_quantity(text, default=0):
    return safe_int(text, default)


def safe_amount(text, default=0.0):
    return normalize_number(text, default)


def safe_date(text, default=None):
    if not text:
        return default
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except (ValueError, TypeError):
            continue
    return default


def safe_note(text, default=""):
    if text is None:
        return default
    return str(text).strip()
