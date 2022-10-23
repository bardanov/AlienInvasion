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

    