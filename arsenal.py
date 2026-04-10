import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class Arsenal:
    """Creates a class to house the ship's arsenal"""

    def __init__(self, game: 'AlienInvasion'):
          """Creates funtion to initialize arsenal"""
          self.game = game
          self.settings = game.settings
          self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
         """Updates the arsenal"""
         self.arsenal.update()
         self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Removes bullets after they exit the screen"""
        for bullet in self.arsenal.copy():
             if bullet.rect.bottom <= 0:
                  self.arsenal.remove(bullet)

         
    def draw(self):
         """draws bullets for the arsenal"""
         for bullet in self.arsenal:
              bullet.draw_bullet()

    def fire_bullet(self):
         """Fires bullets from the arsenal"""
         if len(self.arsenal) < self.settings.bullet_amount:
              new_bullet = Bullet(self.game)
              self.arsenal.add(new_bullet)
              return True
         return False
