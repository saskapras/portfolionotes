# === Stage 40: Add plain text report export ===
# Project: PortfolioNotes
def export_report(self, report_dir="reports"):
    """Export a plain text report of all holdings and notes."""
    import os
    os.makedirs(report_dir, exist_ok=True)
    lines = []
    lines.append("=== PortfolioNotes Report ===")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    for h in self.holdings:
        lines.append(f"--- {h.ticker} ---")
        lines.append(f"Holding: {h.ticker}, Shares: {h.shares}, Avg Cost: ${h.avg_cost:.2f}")
        lines.append(f"Notes: {h.notes}")
        lines.append(f"Reminders: {h.reminders}")
        lines.append("")
    lines.append("=== End of Report ===")
    path = os.path.join(report_dir, "portfolio_report.txt")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    return path
