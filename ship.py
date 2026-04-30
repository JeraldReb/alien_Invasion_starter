"""ship.py
Jerald Reb
Creates the ship for the game
Starter code from units 12, 13, and 14 resources
April 30, 2026"""

import pygame
from settings import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """Creates a class to house the ship"""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Creates a function to initialize the ship"""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        """Centers the ship"""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Updates the ship position on the screen"""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Updates the movement of the ship based on speed and boundaries"""
        temp_speed = self.settings.ship_speed
        
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x


    def draw(self):
        """Draws the ship on the screen"""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Fires the bullets"""
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        """Checks for collisions involving the ship"""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False