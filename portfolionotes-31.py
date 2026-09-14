# === Stage 31: Add compact table rendering for long lists ===
# Project: PortfolioNotes
def render_compact_table(rows, columns, max_rows=15):
    """Render a compact table for long lists, truncating to max_rows."""
    if not rows:
        return ""
    headers = columns
    if len(headers) > 10:
        headers = headers[:10]
    col_widths = [max(len(str(h)) for h in headers)]
    for row in rows[:max_rows]:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    col_widths = [min(w, 20) for w in col_widths]
    separator = "+".join("-" * (w + 2) for w in col_widths)
    lines = [separator]
    header_line = "| " + " | ".join(str(h).center(col_widths[i]) for i, h in enumerate(headers)) + " |"
    lines.append(header_line)
    lines.append(separator)
    for row in rows[:max_rows]:
        line = "| " + " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)) + " |"
        lines.append(line)
    if len(rows) > max_rows:
        lines.append(f"| ... (truncated, {len(rows) - max_rows} more rows) |")
    return "\n".join(lines)
