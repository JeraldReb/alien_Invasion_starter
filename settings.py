import pathlib
from pathlib import Path
class Settings:
    """Creates a class to house game settings"""
    
    def __init__(self):
        """Function to initialize game settings"""
        self.name: str = 'Alien Invasion'
        self.screen_w = 900
        self.screen_h = 600
        self.FPS = 60
        self.bg_file = Path.cwd() / 'alien_Invasion_starter' / 'Assets' / 'images' / 'Starbasesnow.png'
        
        self.ship_file = Path.cwd() / 'alien_Invasion_starter' / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
