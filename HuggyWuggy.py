import pygame, sys

from hw_settings import Settings
from hw_pic import Huggy
from huggy_bullet import Bullet
from alieeeenz import Alieenz

class HuggyWuggy:
    """Main class representing the development of the game."""
    def __init__(self):
        """Block of main game's attributes."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = (self.settings.bg_color)
        self.huggy = Huggy(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        pygame.display.set_caption('Huggy Wuggy')

    def run_game(self):
        """Main loop for launching the game and updating screen and input."""
        while True:
            self.huggy.update()
            self._check_events()
            self._check_screen_updates()
            self._bullets_update()
            self._create_fleet()

    def _check_events(self):
        """Respond to keys and mouse input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.huggy.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.huggy.moving_left = True
        elif event.key == pygame.K_UP:
            self.huggy.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.huggy.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.huggy.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.huggy.moving_left = False
        elif event.key == pygame.K_UP:
            self.huggy.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.huggy.moving_down = False

    def _fire_bullet(self):
        """Fire bullets and add them to the bullets list."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _bullets_update(self):
        """Update the bullets and get rid of old ones."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _create_fleet(self):
        """Create a fleet of aliens."""
        alien = Alieenz(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.huggy.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for rows_number in range(number_rows):
            for aliens_number in range(number_aliens_x):
                self._create_alien(aliens_number, rows_number)

    def _create_alien(self, aliens_number, rows_number):
        """Create aliens and add them to the fleet."""
        alien = Alieenz(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * aliens_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * rows_number 
        self.aliens.add(alien)

    def _check_screen_updates(self):
        """Check the screen updates and surface movements."""
        self.screen.fill(self.settings.bg_color)
        self.huggy.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    hw = HuggyWuggy()
    hw.run_game()
