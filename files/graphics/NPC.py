import pygame_functions

class NPC:
    __init__(self, image, frames, x, y, data):
        self.NPC = makeSprite(image, frames)
        self.NPC_X = x
        self.NPC_Y = y
