# === Stage 16: Add argparse support for the most common commands ===
# Project: PortfolioNotes
import argparse, sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="PortfolioNotes CLI")
    sub = parser.add_subparsers(dest="cmd")

    p = sub.add_parser("add", help="Add a holding")
    p.add_argument("ticker", help="e.g. AAPL")
    p.add_argument("--name", help="Display name")
    p.add_argument("--cost", type=float, help="Cost basis")
    p.add_argument("--qty", type=int, help="Quantity")
    p.add_argument("--note", help="Initial note")
    p.set_defaults(func=lambda a: add_holding(a))

    p = sub.add_parser("list", help="List holdings")
    p.set_defaults(func=lambda a: list_holdings(a))

    p = sub.add_parser("snapshot", help="Record a price snapshot")
    p.add_argument("ticker", help="Ticker")
    p.add_argument("--price", type=float, required=True, help="Price")
    p.add_argument("--date", help="Date (default today)")
    p.add_argument("--note", help="Snapshot note")
    p.set_defaults(func=lambda a: snapshot(a))

    p = sub.add_parser("note", help="Add a note to a holding")
    p.add_argument("ticker", help="Ticker")
    p.add_argument("--text", required=True, help="Note text")
    p.set_defaults(func=lambda a: add_note(a))

    p = sub.add_parser("remind", help="Add a reminder")
    p.add_argument("ticker", help="Ticker")
    p.add_argument("--days", type=int, required=True, help="Days until reminder")
    p.set_defaults(func=lambda a: add_reminder(a))

    p = sub.add_parser("show", help="Show a holding")
    p.add_argument("ticker", help="Ticker")
    p.set_defaults(func=lambda a: show_holding(a))

    args = parser.parse_args()
    if args.cmd is None:
        parser.print_help()
        sys.exit(1)
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)
    args.func(args)
