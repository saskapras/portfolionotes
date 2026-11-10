# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: PortfolioNotes
def main():
    try:
        while True:
            command = input("portfolio> ").strip()
            if command.lower() in ("exit", "quit"):
                break
            execute_command(command)
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
