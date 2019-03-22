from pygame_functions import *

### BG ###
# CONSTANTS #
BG_FRAMES = [  ["images/dungeonFloor1.png", "images/dungeonFloor2.png"] ,
                       ["images/dungeonFloor3.png", "images/dungeonFloor4.png"]  ]
FPS = 120

# SETUP #
X_SIZE = 600
Y_SIZE = 600
X_CENTER = X_SIZE/2
Y_CENTER = Y_SIZE/2
screenSize(600,600) # must be size of bg pic
setAutoUpdate(False)
setBackgroundImage(BG_FRAMES)
### BG ###

### NPC ###
X_NPC = 0
Y_NPC = 0
NPC = makeSprite("images/dungeonWalls.png")
moveSprite(NPC, X_NPC,Y_NPC)
showSprite(NPC)
### NPC ###



### PC ###
# CONSTANTS #
PC_IMAGE = "images/robo.gif"
PC_FRAMES = 16
NEXT_FRAME = clock()
FRAME=0
DIRECTION = 1
PC_CYCLE = 4
REFRESH = 150
L_SPEED = 3
R_SPEED = -3
U_SPEED = 3
D_SPEED = -3


# SETUP #
PC = makeSprite(PC_IMAGE, PC_FRAMES)
moveSprite(PC, X_CENTER, Y_CENTER, True)
showSprite(PC)

# MOVEMENT
while True:
    if clock() > NEXT_FRAME:                        # Refresh timing
        FRAME = (FRAME+1)%PC_CYCLE                # Loop on end
        NEXT_FRAME += REFRESH                      # Next frame
    # collision
    if touching(PC, NPC):
        print(DIRECTION)
        if DIRECTION == 0:  # down
            L_SPEED = 3
            R_SPEED = -3
            U_SPEED = 3
            D_SPEED = 0
        elif DIRECTION == 1:    # left
            L_SPEED = 0
            R_SPEED = -3
            U_SPEED = 3
            D_SPEED = -3
        elif DIRECTION == 2: # right
            L_SPEED = 3
            R_SPEED = 0
            U_SPEED = 3
            D_SPEED = -3
        elif DIRECTION == 3: # up
            L_SPEED = 3
            R_SPEED = -3
            U_SPEED = 0
            D_SPEED = -3
    else:
        L_SPEED = 3
        R_SPEED = -3
        U_SPEED = 3
        D_SPEED = -3


    if keyPressed("down"):
        DIRECTION = 0
        changeSpriteImage(PC, DIRECTION*PC_CYCLE+FRAME)    #  First dir
        scrollBackground(0,D_SPEED)
        Y_NPC +=D_SPEED
        moveSprite(NPC, X_NPC, Y_NPC)
        

    elif keyPressed("left"):
        DIRECTION = 1
        changeSpriteImage(PC, DIRECTION*PC_CYCLE+FRAME)    
        scrollBackground(L_SPEED,0)
        X_NPC += L_SPEED
        moveSprite(NPC, X_NPC, Y_NPC)

    elif keyPressed("right"):
        DIRECTION = 2
        changeSpriteImage(PC, DIRECTION*PC_CYCLE+FRAME)    
        scrollBackground(R_SPEED,0)
        X_NPC += R_SPEED
        moveSprite(NPC, X_NPC, Y_NPC)

    elif keyPressed("up"):
        DIRECTION = 3
        changeSpriteImage(PC,DIRECTION*PC_CYCLE+FRAME)
        scrollBackground(0,U_SPEED)
        Y_NPC += U_SPEED
        moveSprite(NPC, X_NPC, Y_NPC)

    else:
        changeSpriteImage(PC, DIRECTION * PC_CYCLE)  # stop motion

    updateDisplay()
    tick(FPS)

endWait()
