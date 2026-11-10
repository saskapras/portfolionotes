# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: PortfolioNotes
def build_report(data):
    warnings = []
    errors = []
    holdings = data.get("holdings", [])
    notes = data.get("notes", [])
    snapshots = data.get("snapshots", [])
    reminders = data.get("reminders", [])
    for h in holdings:
        if not h.get("ticker"):
            errors.append("holding missing ticker")
        if not h.get("quantity"):
            warnings.append("holding missing quantity")
    for n in notes:
        if not n.get("ticker"):
            errors.append("note missing ticker")
        if not n.get("content") or not n["content"].strip():
            warnings.append("note has empty content")
    for s in snapshots:
        if not s.get("ticker"):
            errors.append("snapshot missing ticker")
        if not s.get("price"):
            errors.append("snapshot missing price")
        if s.get("date"):
            try:
                d = datetime.strptime(s["date"], "%Y-%m-%d")
            except ValueError:
                errors.append("snapshot date invalid: " + str(s["date"]))
    for r in reminders:
        if not r.get("ticker"):
            warnings.append("reminder missing ticker")
        if r.get("due") and datetime.strptime(r["due"], "%Y-%m-%d") < datetime.now():
            warnings.append("reminder overdue: " + str(r["due"]))
    return {"warnings": warnings, "errors": errors}
