# === Stage 55: Add a setting to disable colorized output ===
# Project: PortfolioNotes
class PortfolioConfig:
    def __init__(self):
        self.color = True

    def enable_colors(self):
        self.color = True

    def disable_colors(self):
        self.color = False

    def is_color_enabled(self):
        return self.color
