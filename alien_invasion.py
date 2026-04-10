"""Participation Activity 12
Jerald Reb
Beginning to create Alien Invasion game
Starter code from Unit 12 resources
April 9, 2026"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

class AlienInvasion:
    """Creates a class to house the game"""
    
    def __init__(self):
        """Initializes the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.5)

        self.ship = Ship(self, Arsenal(self))

    def run_game(self):
        """Begins to run the game"""
        # Game Loop
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        """Updates the screen and objects on it"""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        """Checks for user input and responds to it"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Checks for key presses and responds to them"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                # play the laser sound
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
                
    def _check_keyup_events(self, event):
        """Checks for key releases and responds to them"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
