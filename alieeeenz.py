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

    def update(self):
        """Move the fleet to the right and to the left."""
        self.x += self.settings.aliens_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if aliens reach the edge."""
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
