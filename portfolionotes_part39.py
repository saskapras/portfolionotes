# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: PortfolioNotes
def repair_portfolio(path):
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]
    repaired = []
    for i, line in enumerate(lines):
        if line.startswith('HOLDING:'):
            parts = line.split(':')
            if len(parts) >= 3:
                name = parts[1].strip()
                try:
                    qty = float(parts[2].strip())
                except ValueError:
                    qty = 0.0
                try:
                    cost = float(parts[3].strip()) if len(parts) >= 4 else 0.0
                except ValueError:
                    cost = 0.0
                repaired.append(f"HOLDING:{name}:{qty:.4f}:{cost:.4f}")
        elif line.startswith('NOTE:'):
            repaired.append(line)
        elif line.startswith('PRICE:'):
            parts = line.split(':')
            if len(parts) >= 4:
                try:
                    date = parts[1].strip()
                    price = float(parts[3].strip())
                except ValueError:
                    price = 0.0
                repaired.append(f"PRICE:{date}:{price:.4f}")
        elif line.startswith('REMINDER:'):
            parts = line.split(':')
            if len(parts) >= 3:
                try:
                    date = parts[1].strip()
                except ValueError:
                    date = ''
                repaired.append(f"REMINDER:{date}:{parts[2].strip()}")
    with open(path, 'w') as f:
        f.write('\n'.join(repaired) + '\n')
