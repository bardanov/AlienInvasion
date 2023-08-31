import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Main class to develop the sprites of bullets for game."""
    def __init__(self, h_game):
        super().__init__()
        self.screen = h_game.screen
        self.settings = h_game.settings
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, + 
            self.settings.bullet_height)
        self.color = self.settings.bullet_color
        self.rect.midtop = h_game.huggy.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet over the screen."""
        self.rect.y -= self.settings.bullet_speed
        self.y = self.rect.y 

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
