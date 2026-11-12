# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: PortfolioNotes
def self_check():
    print("PortfolioNotes self-check")
    for h in holdings:
        for r in reminders:
            if r["holding"] == h["symbol"]:
                print(f"Reminder for {h['symbol']}: {r['note']}")
    print(f"Total holdings: {len(holdings)}")
    print(f"Total notes: {len(notes)}")
    print(f"Total snapshots: {len(snapshots)}")
    for s in snapshots:
        print(s["symbol"], s["price"], s["date"])
    print("Self-check complete")
self_check()
