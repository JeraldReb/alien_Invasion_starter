"""Participation Activity 12
Jerald Reb
Beginning to create Alien Invasion game
Starter code from Unit 12 resources
April 9, 2026"""

import sys
import pygame
from settings import Settings

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

    def run_game(self):
        """Begins to run the game"""
        # Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg, (0,0))
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
