from pygame_functions import *
### PC ###
class PC:
    def __init__(self, image, x, y, spd, direction, frames, cycle):
        # CONSTANTS #
        self.PC_IMAGE = image
        self.PC_FRAMES = frames
        self.X_PC = x
        self.Y_PC = y
        self.DIRECTION = direction
        self.PC_CYCLE = cycle

        self.L_SPEED = spd
        self.R_SPEED = -spd
        self.U_SPEED = spd
        self.D_SPEED = -spd


        # SETUP #
        self.PC = makeSprite(self.PC_IMAGE, self.PC_FRAMES)
        self.PC_MASK = pygame.mask.from_surface(self.PC.image)
