class GameStats:
    """Statistics for the game."""
    def __init__(self, huggame):
        self.settings = huggame.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics of ships for the game."""
        self.ships_left = self.settings.ships_limit