# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: PortfolioNotes
def format_holding(h):
    """Return a one-line compact summary for a holding."""
    return (
        f"{h.symbol:>8}  qty: {h.quantity:>7}  "
        f"avg_cost: {h.avg_cost:.2f}  "
        f"current: {h.current_price:.2f}  "
        f"pnl: {h.pnl_pct:+.1f}%"
    )

def format_snapshot(s):
    """Return a one-line compact summary for a price snapshot."""
    return (
        f"{s.symbol:>8}  date: {s.date}  "
        f"price: {s.price:.2f}  "
        f"note: {s.note or 'none'}"
    )

def format_reminder(r):
    """Return a one-line compact summary for a reminder."""
    return (
        f"{r.title or 'Reminder':>20}  "
        f"due: {r.date}  "
        f"active: {r.active}"
    )

def format_note(n):
    """Return a one-line compact summary for a note."""
    return (
        f"{n.title or 'Note':>20}  "
        f"created: {n.created}  "
        f"content: {n.content[:50]}{'...' if len(n.content)>50 else ''}"
    )
