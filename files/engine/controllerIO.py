import pygame



class Controller:
    def __init__(self, number):
        self.buttonMap = { 0:"x", 1:"a", 2:"b", 3:"y", 4:"l", 5:"r", 8:"select", 9:"start"} 
        pygame.init()
        ## find controllers
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(number)
        self.joystick.init()
        self.clock = pygame.time.Clock()
        self.done = False

    def getInput(self):
        # EVENT PROCESSING STEP
        pygame.event.get()
        ## axis control ##
        for i in range( 2 ):
            axis = self.joystick.get_axis(i)
            if axis >= 0.9 or axis == -1.0:
                if axis > 0 and i == 0:
                    return "right"
                if axis < 0 and i == 0:
                    return "left"
                if axis > 0 and i == 1:
                    return "down"
                if axis < 0 and i == 1:
                    return "up"
  
        ## button control ##
        for i in range(10):
            button = self.joystick.get_button(i)
            if button == 1:
                return self.buttonMap[i]
        return None
