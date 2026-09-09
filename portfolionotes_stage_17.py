# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: PortfolioNotes
def dry_run_mode():
    """Enable dry-run mode for all mutating commands.

    When dry_run is True, commands that would normally modify state
    will instead print what they would do and return False.
    """
    global _dry_run
    _dry_run = True

def dry_run_command(command):
    """Execute a command in dry-run mode.

    If the command is one of the mutating commands, it will be
    logged and not executed. Otherwise, it will be executed normally.
    """
    if _dry_run:
        print(f"[DRY RUN] Would execute: {command}")
        return False
    else:
        return execute_command(command)

def execute_command(command):
    """Execute a command based on the command type."""
    command = command.strip()
    if command == "add_holding":
        parts = command.split(":", 1)
        if len(parts) != 2:
            print("Invalid add_holding command")
            return False
        symbol, note = parts
        add_holding(note, symbol)
        return True
    elif command == "add_note":
        parts = command.split(":", 1)
        if len(parts) != 2:
            print("Invalid add_note command")
            return False
        symbol, note = parts
        add_note(symbol, note)
        return True
    elif command == "add_price":
        parts = command.split(":", 1)
        if len(parts) != 2:
            print("Invalid add_price command")
            return False
        symbol, price = parts
        add_price(symbol, price)
        return True
    elif command == "add_reminder":
        parts = command.split(":", 1)
        if len(parts) != 2:
            print("Invalid add_reminder command")
            return False
        symbol, reminder = parts
        add_reminder(symbol, reminder)
        return True
    elif command == "list_holdings":
        list_holdings()
        return True
    elif command == "list_notes":
        list_notes()
        return True
    elif command == "list_prices":
        list_prices()
        return True
    elif command == "list_reminders":
        list_reminders()
        return True
    elif command == "clear":
        clear_all()
        return True
    elif command == "help":
        print("Available commands: add_holding, add_note, add_price, add_reminder, list_holdings, list_notes, list_prices, list_reminders, clear, help")
        return True
    else:
        print("Unknown command")
        return False
