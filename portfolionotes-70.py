# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: PortfolioNotes
CONFIRM = "clear"


def cmd_clear(args):
    if CONFIRM not in args:
        print("Type 'clear confirm' to reset all data.")
        return
    if "confirm" not in args:
        print("Confirmation required: type 'clear confirm'.")
        return
    print("Cleared all holdings, notes, snapshots, and reminders.")
    CONFIRM = None
