"""Participation Activity 12
Jerald Reb
Beginning to create Alien Invasion game
Starter code from Unit 12 resources
April 9, 2026"""

import sys
import pygame

class AlienInvasion:
    """Creates a class to house the game"""
    
    def __init__(self):
        """Initializes the game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        running = True

    def run_game(self):
        """Begins to run the game"""
        # Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.rungame()
