import controllerIO
import leveltst1

## controls ##
c = controllerIO.Controller(0) # get first controller

# IMAGES # -- temp
BG_IMAGE = ["images/JBG.png"]
PC_IMAGE = "images/robo.gif"
WALL_IMAGE = [("images/JWALL.png",0,0)]

level = leveltst1.LEVEL(BG_IMAGE, PC_IMAGE, WALL_IMAGE, c)
