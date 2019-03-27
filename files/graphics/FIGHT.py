from pygame_functions import *
import CHARACTER as c
import controllerIO as ct
import _thread
from PygameFunctionClass import *

pg = PygameFunctionClass()
class BATTLE:
    def __init__(self, bg, characters, enemies, controller, x = 600, y = 600,sound = False):
        # SOUND #
        if sound:
            self.BG_MUSIC = makeMusic("sounds/110Fighting.mp3")
            self.MENU_BLIP = makeSound("sounds/DCMenuTing.wav")
            pg.playMusic(3)
        # DATA #
        self.POINTER_BUFFER = -15
        self.ENEMIES = enemies
        self.CHARACTERS = characters
        self.actionDict = {"Fight": self.attack, "Defend": self.defend}
        self.fontSize = int(y/20) #lowest to highest height
        self.menuOffsetY = int(49/60*y)
        self.nameOffsetX = int(1/2*x)
        self.charOffsetX = int(3/4*x)
        self.healthOffsetX = int(3/4*x)
        self.charOffsetY = int(5/12*y)
        self.enemyOffsetY = (1/6*y)
        self.ATB_TIMER = 0
        #init FPS#
        FPS = 12

        ## BG ##
        self.BACKGROUND = pg.screenSize(x, y)
        pg.setBackgroundImage(bg)
        self.ct = controller

        ## MENU ##
        self.menuBox = pg.makeSprite("images/pixelBox.png")
        pg.moveSprite(self.menuBox, 0, 0)
        pg.showSprite(self.menuBox)

        # NAMES ##
        self.names = []
        for i in range(len(self.CHARACTERS)):
            self.names.append(pg.makeLabel(self.CHARACTERS[i].NAME, self.fontSize, self.nameOffsetX, (i *30)+self.menuOffsetY, "white", "fonts/lunchds.ttf", background = 'clear'))
            pg.showLabel(self.names[-1])
        pg.changeLabel(self.names[0], self.CHARACTERS[0].NAME, fontColour= "yellow")


        # HEALTH #
        self.health = []
        for i in range(len(self.CHARACTERS)):
            self.health.append(pg.makeLabel(str(self.CHARACTERS[i].CURRENT_HEALTH), self.fontSize, self.healthOffsetX, (i*30)+self.menuOffsetY, "white", "fonts/lunchds.ttf", background = 'clear'))
            pg.showLabel(self.health[-1])

        # ATB #
        self.ATB = []
        self.ATB_METER = []
        for i in range(len(self.CHARACTERS)):
            self.ATB.append(pg.makeSprite("images/ATB.png"))
            pg.moveSprite(self.ATB[-1], 500, self.menuOffsetY + i * 30)
            pg.showSprite(self.ATB[-1])



        # ENEMY NAMES ##
        self.enames = []
        for i in range(len(self.ENEMIES)):
            self.enames.append(pg.makeLabel(self.ENEMIES[i].NAME, self.fontSize, 50, (i *30)+self.menuOffsetY, "white", "fonts/lunchds.ttf", background = 'clear'))
            pg.showLabel(self.enames[-1])

        ## SPRITES ##
        self.party = []
        self.comb = []
        self.pointer = pg.makeSprite("images/ppointer.png")
        for i in range(len(self.CHARACTERS)):
            self.party.append(makeSprite(self.CHARACTERS[i].BATTLE_IMAGE))
            pg.moveSprite(self.party[-1], self.charOffsetX + i* 15, (i+1) *30+ self.charOffsetY)
            pg.showSprite(self.party[-1])
        for i in range(len(self.ENEMIES)):
            self.comb.append(pg.makeSprite(self.ENEMIES[i].BATTLE_IMAGE))
            pg.moveSprite(self.comb[-1], 50 - i * 15, (i +1)* 75+self.enemyOffsetY)
            pg.showSprite(self.comb[-1])

        pg.moveSprite(self.pointer, self.party[0].rect.center[0], self.party[0].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
        pg.showSprite(self.pointer)

        ## make adjustable menu screen ##

        ## Main loop ##
        self.inBattle = True
        self.prev = None
        self.current = None
        self.charSelect = 0


        ## MAIN LOOP BEGIN ##
        while self.inBattle:
            
            self.button = self.ct.getInput()
            # wait for individual inputs #
            if self.button != self.prev:
                #only input when pressed instead of hold #
                self.prev = self.button
                self.current = self.button
            else:
                self.current = None

            # Character select
            if self.current == "up":
                if self.charSelect > 0:
                    self.charSelect-=1
                    if sound:
                        pg.playSound(self.MENU_BLIP, 0)
                    pg.moveSprite(self.pointer, self.party[self.charSelect].rect.center[0], self.party[self.charSelect].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                    pg.changeLabel(self.names[self.charSelect], self.CHARACTERS[self.charSelect].NAME, fontColour= "yellow")
                    pg.changeLabel(self.names[self.charSelect+1], self.CHARACTERS[self.charSelect+1].NAME, fontColour= "white")
                    pg.updateDisplay()
            if self.current == "down":
                if self.charSelect < len(self.party)-1:
                    self.charSelect+=1
                    if sound:
                        pg.playSound(self.MENU_BLIP, 0)
                    pg.moveSprite(self.pointer, self.party[self.charSelect].rect.center[0], self.party[self.charSelect].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                    pg.changeLabel(self.names[self.charSelect], self.CHARACTERS[self.charSelect].NAME, fontColour= "yellow")
                    pg.changeLabel(self.names[self.charSelect-1], self.CHARACTERS[self.charSelect-1].NAME, fontColour= "white")
                    pg.updateDisplay()
            self.turn = self.charSelect # self.current choice

        ## ACTION MENU##

            if self.current == "a":
                if self.CHARACTERS[self.turn].ATB_START != self.CHARACTERS[self.turn].ATB_MAX:
                    pass
                else:
                    for name in self.enames:
                        pg.hideLabel(name)
                        
                    self.actions = []
                    ## IN MENU ##

                    # INITIALIZE MENU TEXT #
                    for i in range(len(self.CHARACTERS[i].ACTIONS)):
                        self.actions.append(pg.makeLabel(self.CHARACTERS[self.turn].ACTIONS[i], self.fontSize, 50, (i * 30)+ self.menuOffsetY, "white", font ="fonts/lunchds.ttf", background = 'clear'))
                        pg.showLabel(self.actions[-1])
                    pg.changeLabel(self.actions[0], self.CHARACTERS[self.turn].ACTIONS[0], fontColour = "yellow")

                    # IN MENU CONTROL #
                    self.menuOption = 0 # start with first option
                    self.menuOpen = True # menu open option
                    self.menuPrev = "a"
                    self.menuInput = None
                    while self.menuOpen:
                        self.menuButton = self.ct.getInput()
                        if self.menuButton != self.menuPrev:

                            self.menuInput = self.menuButton
                            self.menuPrev = self.menuButton
                        else:
                            self.menuInput = None

                        # ACTION MENU SELECT #
                        if self.menuInput == "up":
                            if self.menuOption > 0:
                                self.menuOption-=1

                                pg.changeLabel(self.actions[self.menuOption], self.CHARACTERS[self.turn].ACTIONS[self.menuOption], fontColour= "yellow")
                                pg.changeLabel(self.actions[self.menuOption+1], self.CHARACTERS[self.turn].ACTIONS[self.menuOption+1], fontColour= "white")
                        elif self.menuInput == "down":
                            if self.menuOption < len(self.actions)-1:
                                self.menuOption+=1

                                pg.changeLabel(self.actions[self.menuOption], self.CHARACTERS[self.turn].ACTIONS[self.menuOption], fontColour= "yellow")
                                pg.changeLabel(self.actions[self.menuOption-1], self.CHARACTERS[self.turn].ACTIONS[self.menuOption-1], fontColour= "white")

                        # PICK ACTION #
                        elif self.menuInput == "a":
                            self.actionDict[self.CHARACTERS[self.turn].ACTIONS[self.menuOption]](self.CHARACTERS[self.turn])
                            self.menuPrev = "b"



                        # CLOSE MENU #
                        elif self.menuInput == "b":
                            for i in range(len(self.actions)):
                                pg.hideLabel(self.actions[i])
                            self.actions = []
                            self.menuOpen = False
                        pg.updateDisplay()
            #end menu loop
                    
            pg.updateDisplay()
            
##            ## ATB TIMER ##
##            for i in range(len(self.CHARACTERS)):
##                drawRect(505, self.menuOffsetY + 6+ i * 30, self.CHARACTERS[i].ATB_START, 14, "green", linewidth = 0)
##
##                if self.CHARACTERS[i].ATB_START < 48:
##                    self.CHARACTERS[i].ATB_START +=self.CHARACTERS[i].ATB_RATE
##                else:
##                    self.CHARACTERS[i].ATB_START = 0
##                    drawRect(505, self.menuOffsetY + 6 + i * 30, self.CHARACTERS[i].ATB_START, 14, (255,255,255,128), linewidth = 0)
##                    

        ##ATB THREAD ##
            _thread.start_new_thread(self.ATBtimer, (None,))
        
            pg.tick(FPS)
            ## all enemies are dead? ##
            if not self.ENEMIES:
                self.inBattle = False
            #end battle loop

        ## END BATTLE MUSIC ##
        if sound:
            pg.stopMusic()
            endMusic = pg.makeMusic("sounds/111Fanfare.mp3")
            pg.playMusic()
        pg.endWait()

    def attack(self, char):
        attackPointer = True
        # move pointer to enemy side
        pg.moveSprite(self.pointer, self.comb[0].rect.center[0], self.comb[0].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
        ## character select ##
        attackPrev = "a"
        attackCurrent = None
        attackCharSelect = 0

        for i in self.actions:
            pg.hideLabel(i)
        for i in self.enames:
            pg.showLabel(i)
        pg.changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "yellow")
        while attackPointer:
            attackButton = self.ct.getInput()
            # wait for individual inputs #
            if attackButton != attackPrev:
                #only input when pressed instead of hold #
                attackPrev = attackButton
                attackCurrent = attackButton
            else:
                attackCurrent = None

            # Character select
            if attackCurrent == "up":
                if attackCharSelect > 0:
                    attackCharSelect-=1

                    pg.moveSprite(self.pointer, self.comb[attackCharSelect].rect.center[0], self.comb[attackCharSelect].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                    pg.changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "yellow")
                    pg.changeLabel(self.enames[attackCharSelect+1], self.ENEMIES[attackCharSelect+1].NAME, fontColour= "white")
            if attackCurrent == "down":
                if attackCharSelect < len(self.comb)-1:
                    attackCharSelect+=1

                    pg.moveSprite(self.pointer, self.comb[attackCharSelect].rect.center[0], self.comb[attackCharSelect].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                    pg.changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "yellow")
                    pg.changeLabel(self.enames[attackCharSelect-1], self.ENEMIES[attackCharSelect-1].NAME, fontColour= "white")

                    
            if attackCurrent == "a":
                ## boy, look at all of this action ##
                self.ENEMIES[attackCharSelect].CURRENT_HEALTH -= char.ATTACK
                pg.changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "white")
                print(self.ENEMIES[attackCharSelect].CURRENT_HEALTH)
                if(self.ENEMIES[attackCharSelect].CURRENT_HEALTH <= 0):
                    pg.hideSprite(self.comb[attackCharSelect])
                    pg.hideLabel(self.enames[attackCharSelect])
                    del self.enames[attackCharSelect]
                    del self.comb[attackCharSelect]
                    del self.ENEMIES[attackCharSelect]
                ## same as press b in menu
                for i in range(len(self.actions)):
                    pg.hideLabel(self.actions[i])
                self.actions = []
                #menu esc
                self.menuOpen = False
                #escape attack
                attackPointer = False
                # move pointer back to original
                pg.moveSprite(self.pointer, self.party[self.turn].rect.center[0], self.party[self.turn].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                self.CHARACTERS[self.turn].ATB_START = 0
                
            if attackCurrent == "b":
                pg.changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "white")
                for i in self.actions:
                    pg.showLabel(i)
                for i in self.enames:
                    pg.hideLabel(i)
                pg.moveSprite(self.pointer, self.party[self.turn].rect.center[0], self.party[self.turn].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                # go back to action menu
                attackPointer = False
        pg.updateDisplay()


    def defend(self, char):
        ## same as press b in menu
        for i in range(len(self.actions)):
            pg.hideLabel(self.actions[i])
        self.actions = []
        #menu esc
        self.menuOpen = False
        #escape attack
        attackPointer = False
        # move pointer back to original
        pg.moveSprite(self.pointer, self.party[self.turn].rect.center[0], self.party[self.turn].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
        print(char.NAME,"defended")
        return None

    def ATBtimer(self, n):
         for i in range(len(self.CHARACTERS)):
                pg.drawRect(506, self.menuOffsetY + 6+ i * 30, self.CHARACTERS[i].ATB_START, 14, "green", linewidth = 0)

                if self.CHARACTERS[i].ATB_START < self.CHARACTERS[self.turn].ATB_MAX:
                    self.CHARACTERS[i].ATB_START +=self.CHARACTERS[i].ATB_RATE
                else:
                   pg.drawRect(506, self.menuOffsetY + 6+ i * 30, self.CHARACTERS[i].ATB_START, 14, "green", linewidth = 0)
 

enem = ["images/mariorpg_bundt.gif",None, 20, 20, 20, "Cake0", ["Fight", "Defend"],0,1, 48]
data = ["images/starmanMINI.png",None, 10,10,10, "Starman0", ["Fight", "Defend"],0, 1, 48]
char = []
combatants = []
for i in range(3):
    char.append(c.CHARACTER(data))
    data[5] = data[5][:-1]+str(i+1)
    data[8] = i+1
for i in range(2):
    combatants.append(c.CHARACTER(enem))
    enem[5] = enem[5][:-1]+ str(i+1)
cont = ct.Controller(0)
fight = BATTLE("images/battleBG.png", char, combatants, cont, 600, 600, False)
