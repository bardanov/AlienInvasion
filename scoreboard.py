import pygame.font

class Scoreboard:
    """Class representing scores for the game."""
    def __init__(self, huggame):
        self.screen = huggame.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = huggame.settings
        self.stats = huggame.stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_highscore()
        self.prep_level()

    def prep_score(self):
        """Turn the str into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, 
            self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highscore(self):
        """Turn the highscore into the rendered image."""
        rounded_highscore = round(self.stats.high_score, -1)
        highscore_str = "{:,}".format(rounded_highscore)
        self.highscore_image = self.font.render(highscore_str, True, 
            self.text_color, self.settings.bg_color)
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn level into the rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, 
            self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def highscore_check(self):
        """Check and change highscore throughout the game."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score 
            self.prep_highscore()

    def show_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)