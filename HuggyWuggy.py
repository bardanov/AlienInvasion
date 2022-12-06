import pygame, sys
from time import sleep

from hw_settings import Settings
from hw_pic import Huggy
from huggy_bullet import Bullet
from alieeeenz import Alieenz
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from left_ships import LeftShips

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
        self.l_ships = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        pygame.display.set_caption('Huggy Wuggy')
        self.button = Button(self, 'Play Game')
        self.sb = Scoreboard(self)
        # It seemed a bit strange first that 'create fleet' needed to be present
        # also in _init_ to call this method right from here.
        self._create_fleet()

    def run_game(self):
        """Main loop for launching the game and updating screen and input."""
        while True:
            self._check_events()
            # We put 'check events' before the 'if' block because we still need
            # the game to react to mouse and keys input while the game is in
            # inactive mode.
            if self.stats.game_active == True:
                self.huggy.update()
                self._bullets_update()
                self._aliens_update()
            self._check_screen_updates()
            # Wet put 'screen updates' outside and after 'if' block because
            # this too is needed to keep updating the screen each iteration
            # in spite of the code in 'if' block.

    def _check_events(self):
        """Respond to keys and mouse input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                # This 'get_pose' function returns us the pixel coordinates
                # of your mouse position and assigns this data to the 'mouse_pose'
                # variable.

    def _check_play_button(self, mouse_pos):
        """Start game if the Play button is pushed."""
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        # We assign the area where the mouse input is only considered to be
        # inside of the 'Play' button rect.
        if button_clicked and not self.stats.game_active:
            self._start_game()
            # If the button of the assigned to the mouse area is clicked by that
            # mouse while the game is is inactive state, we call the 'start game'
            # function. 
                
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
        # elif event.key == pygame.K_UP:
        #     self.huggy.moving_up = True
        # elif event.key == pygame.K_DOWN:
        #     self.huggy.moving_down = True

        # I turn off this block of code because the current version of the game
        # doesn't need the character to go up or down, only right of left. This 
        # was just my part of self studies and the possibilities exploration.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.huggy.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.huggy.moving_left = False
        # elif event.key == pygame.K_UP:
        #     self.huggy.moving_up = False
        # elif event.key == pygame.K_DOWN:
        #     self.huggy.moving_down = False

        # I turn off this block of code because the current version of the game
        # doesn't need the character to go up or down, only right of left. This 
        # was just my part of self studies and the possibilities exploration. 

    def _start_game(self):
        """Start game if the P button is pressed."""
        if not self.stats.game_active:
            self.stats.reset_stats()
            self.sb.prep_level()
            self.sb.prep_score()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self._l_ships()
            self.huggy.center_ship()
            pygame.mouse.set_visible(False)
            # We turn off the visibility of the mouse cursor before returning
            # to the active game.
            self.settings.initialize_dynamic_settings()

    def _l_ships(self):
        """Show how many ships are left."""
        l_ship = LeftShips(self)

        for ship_number in range(self.stats.ships_left):
            l_ship = LeftShips(self)
            l_ship.x = 10 + ship_number * l_ship.rect.width
            l_ship.rect.x = l_ship.x
            l_ship.rect.y = 20
            self.l_ships.add(l_ship)
    # This and the following methods I wrote for the sprites representing the
    # little and cropped pics of the Huggy as the indicator of remaining ships
    # number because I did not want to use the full-height pic and the same rect of
    # the Ship Huggy Pic.

    def count_lships(self):
        """Check the amount of ships left."""
        for ship in self.l_ships.copy():
            self.l_ships.remove(ship)
    # This method is called from 'Ship hit' to remove one ship indicator from
    # the sprites if the ship is hit by a alien. Also here we need to call the  
    # previous '_l_ships' method to update the number of the Huggy ships   
    # pictures after deleting one.
            self._l_ships()

    def _fire_bullet(self):
        """Fire bullets and add them to the bullets list."""
        if len(self.bullets) < self.settings.bullets_allowed:
            # Here we're limiting the number of bullets that can be shot
            # and simultaneously fly on the screen.
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _bullets_update(self):
        """Update the bullets and get rid of old ones."""
        self.bullets.update()
        self._check_bullets_aliens_collide()

        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        # Removing the bullets once they fly off the top of the screen because
        # if we don't delete them they will fly forever up on the y-coordinate
        # and use the memory slowing the game.

        #print(len(self.bullets))

    def _check_bullets_aliens_collide(self):
        """Respond appropriately to the aliens and bullets collisions."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        # This Pygame function turns on collisions of the first two rects we 
        # pass it as arguments and the last two arguments adjust the details of
        # collisions. 'True' means the fist rect disappears after hitting the
        # second rect and can't hit anything else.

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.highscore_check()
        # Also the collisions function retuns a dictionary of the rects we 
        # hit and here we make sure we mention, make disappear and, most topical,
        # count in the scores all the hit aliens.

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
        alien.rect.y += 27
        # I had to also put the aliens fleet to the 27 pixels down starting
        # position because otherwise the upper line of the fleet intersected
        # the scoring rect.
        self.aliens.add(alien)

    def _aliens_update(self):
        """Update the aliens' position on the screen."""
        self.aliens.update()
        self._check_fleet_edge()
        self._check_aliens_bottom()

        if pygame.sprite.spritecollideany(self.huggy, self.aliens):
            self._ship_hit()
        # Here we make the game react when any of the aliens reach the Huggy
        # ship.

    def _ship_hit(self):
        """Respond if aliens manage to hit the ship."""
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.count_lships()
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.huggy.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            # The mouse cursor is visible and active when the game is stopped
            # and the green 'Play game' button appears.

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
        # The fleet direction is set to 1 which means the fleet is moving right.
        # But when it reaches the screen edge, we multiply the number on -1 which
        # gives us -1 and makes the fleet move to the left until it hits edge again.

    def _check_screen_updates(self):
        """Check the screen updates and surface movements."""
        self.screen.fill(self.settings.bg_color)
        self.huggy.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        self.sb.show_score()

        # Here we need to pay attention to the types of rects to make seen on
        # the screen. If we draw one rect made of picture, we use 'blitme' and
        # if it's sprites with pic or created with pixels Rect, we use 'screen.
        # draw' with different screen and pic arguments passed to them.

        self.l_ships.draw(self.screen)

        if not self.stats.game_active:
            self.button.draw_button()
        # Here we draw the 'Play' button on the screen only when the game is in
        # inactive state.

        pygame.display.flip()

if __name__ == '__main__':
    hw = HuggyWuggy()
    hw.run_game()
