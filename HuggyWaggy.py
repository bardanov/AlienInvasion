import pygame, sys

class HuggyWuggy:
    """Main class representing the development of the game."""
    def __init__(self):
        """Block of main game's attributes."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (102, 140, 255)
        pygame.display.set_caption('Huggy Wuggy')

    def run_game(self):
        """Main loop for launching the game and updating screen and input."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    hw = HuggyWuggy()
    hw.run_game()
