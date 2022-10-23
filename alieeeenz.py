import pygame
from pygame.sprite import Sprite

class Alieenz(Sprite):
    """Class to develops the game'z alienzz."""
    def __init__(self, huggame):
        super().__init__()
        self.screen = huggame.screen
        self.settings = huggame.settings
        self.image = pygame.image.load('alien.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        self.sreen_rect = self.screen.get_rect()
        if self.rect.right >= self.sreen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed
                            * self.settings.fleet_direction)
        self.rect.x = self.x
