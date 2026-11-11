# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: PortfolioNotes
def parse_price_snapshot(line):
    tokens = line.split(',')
    try:
        return tokens[0].strip(), float(tokens[1])
    except (ValueError, IndexError):
        return tokens[0].strip(), 0.0


def format_price(value):
    return f"{value:.2f}"


def parse_reminder(line):
    tokens = line.split(',')
    try:
        return tokens[0].strip(), int(tokens[1]), tokens[2].strip()
    except (ValueError, IndexError):
        return tokens[0].strip(), 0, tokens[2].strip()


def calculate_total_value(holdings, price_map):
    total = 0.0
    for holding in holdings:
        tokens = holding.split(',')
        try:
            name = tokens[0].strip()
            quantity = float(tokens[1])
            price = price_map.get(name, 0.0)
            total += quantity * price
        except (ValueError, IndexError):
            continue
    return total


def is_reminder_due(reminders, today):
    due = []
    for reminder in reminders:
        name, date, text = parse_reminder(reminder)
        if name == today:
            due.append((name, text))
    return due


def format_report(holdings, reminders, today):
    lines = []
    lines.append(f"Report for {today}")
    lines.append("")
    for holding in holdings:
        name = parse_price_snapshot(holding)[0]
        lines.append(f"  {name}")
    lines.append("")
    due = is_reminder_due(reminders, today)
    if due:
        lines.append("Reminders:")
        for name, text in due:
            lines.append(f"  - {text}")
    else:
        lines.append("No reminders for today")
    return "\n".join(lines)
