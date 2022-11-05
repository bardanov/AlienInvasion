class Settings:
    """Settings for 'Huggy Wuggy' game."""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (102, 140, 255)
        self.huggy_speed = 1.5
        self.bullet_speed = 0.5
        self.bullet_color = (15, 15, 15)
        self.bullet_width = 13
        self.bullet_height = 13
        self.bullets_allowed = 2
        self.aliens_speed = 0.4
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ships_limit = 2