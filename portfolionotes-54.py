# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: PortfolioNotes
def colorize(text: str, color: str) -> str:
    """Apply ANSI color codes to text, returning it unchanged if color is None."""
    codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "bold": "\033[1m",
        "reset": "\033[0m",
    }
    if color not in codes:
        return text
    return codes[color] + text + codes["reset"]
