from pygame_functions import *
import PC
import BG
import WALL
import controllerIO



class LEVEL:
    def __init__(self, bg, pc, wall, controller):
        c = controller
        # IMAGES # -- temp
        BG_IMAGE = bg
        PC_IMAGE = pc
        WALL_IMAGE = wall

        # TIMING SETUP #
        FPS = 120
        setAutoUpdate(False)
        REFRESH = 150
        NEXT_FRAME = clock()
        FRAME = 0


        ### SETUP BG ###
        BG_LEVEL = BG.BG(BG_IMAGE, x = 600, y = 600)
        screenSize(BG_LEVEL.X_SIZE, BG_LEVEL.Y_SIZE)
        setBackgroundImage(BG_LEVEL.TILES)


        WALL_LEVEL = WALL.WALL(WALL_IMAGE, 0, 0)
        moveSprite(WALL_LEVEL.WALL_SPRITE, WALL_LEVEL.X_WALL, WALL_LEVEL.Y_WALL)
        showSprite(WALL_LEVEL.WALL_SPRITE)
        ### WALLS ###



        PC_LEVEL = PC.PC(PC_IMAGE, BG_LEVEL.X_CENTER, BG_LEVEL.Y_CENTER, spd = 3, direction = 1, frames = 16, cycle = 4 )
        moveSprite(PC_LEVEL.PC, BG_LEVEL.X_CENTER, BG_LEVEL.Y_CENTER, True)
        showSprite(PC_LEVEL.PC)

        # MOVEMENT
        while True:
            button = c.getInput()
            if clock() > NEXT_FRAME:                        # Refresh timing
                FRAME = (FRAME+1)%PC_LEVEL.PC_CYCLE                # Loop on end
                NEXT_FRAME += REFRESH                      # Next frame
            # collision
            if touching(PC_LEVEL.PC, WALL_LEVEL.WALL_SPRITE):
                print(PC_LEVEL.DIRECTION)
                if PC_LEVEL.DIRECTION == 0:  # down
                    L_SPEED = PC_LEVEL.L_SPEED
                    R_SPEED = PC_LEVEL.R_SPEED
                    U_SPEED = PC_LEVEL.U_SPEED
                    D_SPEED = 0
                elif PC_LEVEL.DIRECTION == 1:    # left
                    L_SPEED = 0
                    R_SPEED = PC_LEVEL.R_SPEED
                    U_SPEED = PC_LEVEL.U_SPEED
                    D_SPEED = PC_LEVEL.D_SPEED
                elif PC_LEVEL.DIRECTION == 2: # right
                    L_SPEED = PC_LEVEL.L_SPEED
                    R_SPEED = 0
                    U_SPEED = PC_LEVEL.U_SPEED
                    D_SPEED = PC_LEVEL.D_SPEED
                elif PC_LEVEL.DIRECTION == 3: # up
                    L_SPEED = PC_LEVEL.L_SPEED
                    R_SPEED = PC_LEVEL.R_SPEED
                    U_SPEED = 0
                    D_SPEED = PC_LEVEL.D_SPEED
            else:
                L_SPEED = PC_LEVEL.L_SPEED
                R_SPEED = PC_LEVEL.R_SPEED
                U_SPEED = PC_LEVEL.U_SPEED
                D_SPEED = PC_LEVEL.D_SPEED


            if keyPressed("down") or button == "down":
                PC_LEVEL.DIRECTION = 0
                changeSpriteImage(PC_LEVEL.PC, PC_LEVEL.DIRECTION*PC_LEVEL.PC_CYCLE+FRAME)    #  First dir
                scrollBackground(0,D_SPEED)
                WALL_LEVEL.Y_WALL +=D_SPEED
                moveSprite(WALL_LEVEL.WALL_SPRITE, WALL_LEVEL.X_WALL, WALL_LEVEL.Y_WALL)


            elif keyPressed("left") or button == "left":
                PC_LEVEL.DIRECTION = 1
                changeSpriteImage(PC_LEVEL.PC, PC_LEVEL.DIRECTION*PC_LEVEL.PC_CYCLE+FRAME)
                scrollBackground(L_SPEED,0)
                WALL_LEVEL.X_WALL += L_SPEED
                moveSprite(WALL_LEVEL.WALL_SPRITE, WALL_LEVEL.X_WALL, WALL_LEVEL.Y_WALL)

            elif keyPressed("right") or button == "right":
                PC_LEVEL.DIRECTION = 2
                changeSpriteImage(PC_LEVEL.PC, PC_LEVEL.DIRECTION*PC_LEVEL.PC_CYCLE+FRAME)
                scrollBackground(R_SPEED,0)
                WALL_LEVEL.X_WALL += R_SPEED
                moveSprite(WALL_LEVEL.WALL_SPRITE, WALL_LEVEL.X_WALL, WALL_LEVEL.Y_WALL)

            elif keyPressed("up") or button == "up":
                PC_LEVEL.DIRECTION = 3
                changeSpriteImage(PC_LEVEL.PC,PC_LEVEL.DIRECTION*PC_LEVEL.PC_CYCLE+FRAME)
                scrollBackground(0,U_SPEED)
                WALL_LEVEL.Y_WALL += U_SPEED
                moveSprite(WALL_LEVEL.WALL_SPRITE, WALL_LEVEL.X_WALL, WALL_LEVEL.Y_WALL)

            else:
                changeSpriteImage(PC_LEVEL.PC, PC_LEVEL.DIRECTION * PC_LEVEL.PC_CYCLE)  # stop motion

            updateDisplay()
            tick(FPS)

        endWait()
