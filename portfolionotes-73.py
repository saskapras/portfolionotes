# === Stage 73: Add a lightweight HTML report export ===
# Project: PortfolioNotes
def export_report(path, holdings, snapshots, notes, reminders):
    with open(path, "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html><head><meta charset='utf-8'><title>PortfolioNotes</title>")
        f.write("<style>body{font-family:sans-serif;margin:2rem}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:6px;text-align:left}</style></head><body>")
        f.write("<h1>Portfolio Report</h1>")
        f.write("<h2>Holdings</h2><table><tr><th>Symbol</th><th>Note</th><th>Last Price</th></tr>")
        for h in holdings:
            last = None
            for s in snapshots:
                if s["symbol"] == h["symbol"]:
                    last = s["price"]
            f.write("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (h["symbol"], h.get("note", ""), last))
        f.write("</table>")
        f.write("<h2>Notes</h2><ul>")
        for n in notes:
            f.write("<li>%s</li>" % n["text"])
        f.write("</ul>")
        f.write("<h2>Reminders</h2><ul>")
        for r in reminders:
            f.write("<li>%s</li>" % r["text"])
        f.write("</ul></body></html>")
