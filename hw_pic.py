import pygame

from hw_settings import Settings

class Huggy:
    """A class modeling the pic object for the game.""" 
    def __init__(self, hw_game):
        self.settings = Settings()
        self.screen = hw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('hw.jpg')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the image to the screen."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the object over the screen surface."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.huggy_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.huggy_speed
        elif self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.huggy_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.huggy_speed

    def center_ship(self):
        """Put the ship in the center of the screen."""
        self.rect.midbottom = self.screen_rect.midbottom