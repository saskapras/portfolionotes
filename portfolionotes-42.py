# === Stage 42: Add CSV export without external dependencies ===
# Project: PortfolioNotes
import csv

def export_to_csv(holdings, notes, snapshots, reminders, filename="portfolio_export.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["type", "symbol", "name", "quantity", "avg_cost", "current_price",
                          "note", "created_at", "updated_at", "due_date", "message"])
        for h in holdings:
            writer.writerow([
                "holding", h["symbol"], h["name"], h["quantity"], h["avg_cost"],
                h.get("current_price", ""), h.get("note", ""), h.get("created_at", ""),
                h.get("updated_at", ""), h.get("due_date", ""), h.get("message", "")
            ])
        for n in notes:
            writer.writerow([
                "note", n.get("symbol", ""), n.get("name", ""), n.get("quantity", ""),
                n.get("avg_cost", ""), n.get("current_price", ""), n.get("content", ""),
                n.get("created_at", ""), n.get("updated_at", ""), "", ""
            ])
        for s in snapshots:
            writer.writerow([
                "snapshot", s.get("symbol", ""), s.get("name", ""), s.get("quantity", ""),
                s.get("avg_cost", ""), s.get("price", ""), s.get("date", ""),
                "", "", "", ""
            ])
        for r in reminders:
            writer.writerow([
                "reminder", r.get("symbol", ""), r.get("name", ""), r.get("quantity", ""),
                r.get("avg_cost", ""), r.get("current_price", ""), r.get("note", ""),
                r.get("created_at", ""), r.get("updated_at", ""), r.get("due_date", ""),
                r.get("message", "")
            ])
