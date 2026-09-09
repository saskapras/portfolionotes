# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: PortfolioNotes
def parse_command(text):
    """Parse a text command into a (command, args) tuple."""
    parts = text.strip().split(None, 1)
    cmd = parts[0].lower()
    arg = parts[1].strip() if len(parts) > 1 else ""
    return cmd, arg
