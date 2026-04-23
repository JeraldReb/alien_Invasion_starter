"""Participation Activity 14
Jerald Reb
Continuing to create Alien Invasion game
Starter code from Unit 12, 13, and 14 resources
April 15, 2026"""

import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion:
    """Creates a class to house the game"""
    
    def __init__(self):
        """Initializes the game"""
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.5)
        self.impact = pygame.mixer.Sound(self.settings.impact)
        self.impact.set_volume(0.5)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, 'Play')
        self.game_active = False

    def run_game(self):
        """Begins to run the game"""
        # Game Loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """checks for collisions between objects"""
        # check for collisions between ship and aliens
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self.check_game_status()

        # checks for collisions between aliens and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self.check_game_status()
        
        # checks for collisions between aliens and bullets
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact.play()
            self.impact.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()

    def check_game_status(self):
        """Checks the status of the game"""
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)

        else:
            self.game_active = False

    def _reset_level(self):
        """Resets level upon completion"""
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        """Restarts the game"""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        """Updates the screen and objects on it"""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        """Checks for user input and responds to it"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """Checks if the play button has been clicked"""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def _check_keydown_events(self, event):
        """Checks for key presses and responds to them"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                # play the laser sound
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()
                
    def _check_keyup_events(self, event):
        """Checks for key releases and responds to them"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
