import pygame
from settings import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    """Creates a class to house the ship"""

    def __init__(self, game: 'AlienInvasion'):
        """Creates a function to initialize the ship"""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        """Updates the ship position on the screen"""
        temp_speed = self.settings.ship_speed
        
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x


    def draw(self):
        """Draws the ship on the screen"""
        self.screen.blit(self.image, self.rect)
