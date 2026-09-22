# === Stage 53: Add command help text and usage examples ===
# Project: PortfolioNotes
def print_help():
    print("PortfolioNotes - Investment Note Tracker")
    print("Usage: python main.py <command>")
    print("Commands:")
    print("  add     Add a new note")
    print("  view    View all notes")
    print("  search  Search notes by keyword")
    print("  history View price history for a stock")
    print("  reminder Set a price reminder")
    print("  help    Show this help message")
    print("Examples:")
    print("  python main.py add -t AAPL -n 'Strong buy at 150'")
    print("  python main.py view")
    print("  python main.py search AAPL")
    print("  python main.py history AAPL")
    print("  python main.py reminder AAPL 160")
    print("  python main.py help")
