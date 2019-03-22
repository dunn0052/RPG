from pygame_functions import *

class CHARACTER:
    def __init__(self, data):
        self.BATTLE_IMAGE = data[0]
        self.LEVEL_IMAGE = data[1]
        self.ATTACK = data[2]
        self.HEALTH = data[3]
        self.MAGIC = data[4]
        self.NAME = data[5]
        self.CURRENT_HEALTH = self.HEALTH
        self.ACTIONS = data[6]
        self.ATB_START = data[7]
        self.ATB_RATE = data[8]
        self.ATB_MAX = data[9]
