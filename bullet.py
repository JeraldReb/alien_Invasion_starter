"""bullet.py
Jerald Reb
Creates the individual bullets for the arsenal
Starter code from units 12, 13, and 14 resources
April 30, 2026"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Creates a class to house bullets for the arsenal"""

    def __init__(self, game: 'AlienInvasion'):
        """Initializes a function for the bullets in the arsenal"""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_w, self.settings.bullet_h))

        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Updates the bullets as they are fired"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullets on the screen"""
        self.screen.blit(self.image, self.rect)