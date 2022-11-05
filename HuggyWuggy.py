import pygame, sys
from time import sleep

from hw_settings import Settings
from hw_pic import Huggy
from huggy_bullet import Bullet
from alieeeenz import Alieenz
from game_stats import GameStats

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
        self.stats = GameStats(self)
        self.huggy = Huggy(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        pygame.display.set_caption('Huggy Wuggy')

        self._create_fleet()

    def run_game(self):
        """Main loop for launching the game and updating screen and input."""
        while True:
            self._check_events()
            if self.stats.game_active == True:
                self.huggy.update()
                self._check_screen_updates()
                self._bullets_update()
                self._aliens_update()

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
        self._check_bullets_aliens_collide()

        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _check_bullets_aliens_collide(self):
        """Respond appropriately to the aliens and bullets collisions."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

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

    def _aliens_update(self):
        """Update the aliens' position on the screen."""
        self.aliens.update()
        self._check_fleet_edge()
        self._check_aliens_bottom()

        if pygame.sprite.spritecollideany(self.huggy, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """Respond if aliens manage to hit the ship."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.huggy.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Respond if aliens manage to reach the bottom."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    def _check_fleet_edge(self):
        """Respond appropriately if any of aliens reach the screen edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet row down and change the direction on x-coord."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

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
