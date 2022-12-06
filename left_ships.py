import pygame
from pygame.sprite import Sprite

class LeftShips(Sprite):
    """Class to develops the game'z alienzz."""
    def __init__(self, huggame):
        super().__init__()
        self.screen = huggame.screen
        self.settings = huggame.settings
        self.image = pygame.image.load('hw_ships.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + 5
        self.rect.y = self.rect.height 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)