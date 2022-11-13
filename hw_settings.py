class Settings:
    """Settings for 'Huggy Wuggy' game."""
    def __init__(self):
        """Initialize static settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (102, 140, 255)
        self.bullet_color = (15, 15, 15)
        self.bullet_width = 13
        self.bullet_height = 13
        self.bullets_allowed = 2
        self.ships_limit = 2
        self.speedup_scale = 1.1
        self.scoreup_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.huggy_speed = 1.5
        self.bullet_speed = 0.5
        self.aliens_speed = 0.4
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase the speed of these statisctics."""
        self.huggy_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.aliens_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.scoreup_scale)





