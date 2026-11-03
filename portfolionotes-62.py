# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: PortfolioNotes
def score_holding(holding):
    score = 0
    if holding.get("price") is not None and holding.get("cost") is not None:
        score += int((holding["price"] - holding["cost"]) / holding["cost"] * 100)
    if holding.get("note") and holding["note"].lower().find("buy") >= 0:
        score += 20
    if holding.get("note") and holding["note"].lower().find("sell") >= 0:
        score -= 20
    if holding.get("note") and holding["note"].lower().find("watch") >= 0:
        score -= 10
    if holding.get("reminders"):
        score += 5 * len(holding["reminders"])
    else:
        score -= 10
    return score
