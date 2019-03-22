from pygame_functions import *
## setup background
class BG:
    def __init__(self, tiles, x = 600, y = 600):
        self.TILES = tiles
        self.X_SIZE = x
        self.Y_SIZE = y
        self.X_CENTER = self.X_SIZE/2
        self.Y_CENTER = self.Y_SIZE/2
