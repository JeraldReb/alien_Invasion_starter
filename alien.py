"""Alien.py
Jerald Reb
Creates the individual aliens for the fleet
Starter code from units 12, 13, and 14 resources
April 30, 2026"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Creates a class to house aliens for the fleet"""

    def __init__(self, fleet: 'AlienFleet', x: int, y: int):
        """Initializes a function for the aliens in the fleet"""
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.y = int(self.rect.y)
        self.x = int(self.rect.x)

    def update(self):
        """Updates the aliens as they move"""
        temp_speed = self.settings.fleet_speed

        # if self.check_edges():
            # self.settings.fleet_direction *= -1
            # self.y += self.settings.fleet_drop_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Checks the boundaries of the screen against the alien fleet"""
        return(self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self):
        """draws the aliens to the screen"""
        self.screen.blit(self.image, self.rect)