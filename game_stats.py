class GameStats:
    """Statistics for the game."""
    def __init__(self, huggame):
        self.settings = huggame.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 1

    def reset_stats(self):
        """Initialize statistics of ships for the game."""
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1
