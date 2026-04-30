"""game_stats.py
Jerald Reb
Holds the stats for the game
Starter code from units 12, 13, and 14 resources
April 30, 2026"""

# from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats:
    """Creates a class to house the game stats"""

    def __init__(self, game: 'AlienInvasion'):
        """Initializes the game stats"""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Retrieves saved scores"""
        self.path = self.settings.scores_file
        if self.path.exists and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """Saves scores to file"""
        scores = {'hi_score': self.hi_score}
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """Resets the game's stats"""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Updates the game scores"""
        # update score
        self._update_score(collisions)

        # update max score
        self._update_max_score()

        # update hi-score
        self._update_hi_score()

    def _update_max_score(self):
        """Updates the max score"""
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'Max: {self.max_score}')

    def _update_hi_score(self):
        """Updates the hi score"""
        if self.score > self.hi_score:
            self.hi_score = self.score
        # print(f'Hi: {self.hi_score}')

    def _update_score(self, collisions):
        """Updates the score"""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f'Score: {self.score}')

    def update_level(self):
        """Updates the level"""
        self.level += 1
        # print(self.level)

    