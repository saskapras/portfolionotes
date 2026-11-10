# === Stage 72: Add Markdown report export ===
# Project: PortfolioNotes
def export_markdown(path, holdings, snapshots, notes, reminders):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('# PortfolioNotes Report\n\n')
        f.write('## Holdings\n')
        for h in holdings:
            f.write(f'- {h["symbol"]}: {h["qty"]} @ {h["avg_cost"]}\n')
        f.write('\n## Price Snapshots\n')
        for s in snapshots:
            f.write(f'- {s["symbol"]}: {s["date"]} -> {s["price"]}\n')
        f.write('\n## Notes\n')
        for n in notes:
            f.write(f'### {n["symbol"]}\n\n{n["text"]}\n\n')
        f.write('\n## Reminders\n')
        for r in reminders:
            f.write(f'- {r["text"]} ({r["date"]})\n')
