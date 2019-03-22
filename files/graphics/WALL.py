from pygame_functions import *
### WALLS ###
class WALL:
    def __init__(self, image, x = 0, y = 0):
        self.WALL_IMAGE = image
        self.X_WALL = x
        self.Y_WALL = y
        self.WALL_SPRITE = makeSprite(self.WALL_IMAGE)
        self.WALL_MASK = pygame.mask.from_surface(self.WALL_SPRITE.image)
