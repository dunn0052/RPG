from pygame_functions import *
import CHARACTER as c
import controllerIO as ct


class BATTLE:
    def __init__(self, bg, characters, enemies, controller, x = 600, y = 600):
        # SOUND #
        bgMusic = makeMusic("sounds/110Fighting.mp3")
        menuBlip = makeSound("sounds/DCMenuTing.wav")
        playMusic(3)
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
        #init FPS#
        FPS = 12

        ## BG ##
        screenSize(x, y)
        setBackgroundImage(bg)
        self.ct = controller

        ## MENU ##
        self.menuBox = makeSprite("images/pixelBox.png")
        moveSprite(self.menuBox, 0, 0)
        showSprite(self.menuBox)

        # NAMES ##
        self.names = []
        for i in range(len(self.CHARACTERS)):
            self.names.append(makeLabel(self.CHARACTERS[i].NAME, self.fontSize, self.nameOffsetX, (i *30)+self.menuOffsetY, "white", "fonts/lunchds.ttf", background = 'clear'))
            showLabel(self.names[-1])
        changeLabel(self.names[0], self.CHARACTERS[0].NAME, fontColour= "yellow")


        # HEALTH #
        self.health = []
        for i in range(len(self.CHARACTERS)):
            self.health.append(makeLabel(str(self.CHARACTERS[i].CURRENT_HEALTH), self.fontSize, self.healthOffsetX, (i*30)+self.menuOffsetY, "white", "fonts/lunchds.ttf", background = 'clear'))
            showLabel(self.health[-1])

        # ENEMY NAMES ##
        self.enames = []
        for i in range(len(self.ENEMIES)):
            self.enames.append(makeLabel(self.ENEMIES[i].NAME, self.fontSize, 50, (i *30)+self.menuOffsetY, "white", "fonts/lunchds.ttf", background = 'clear'))
            showLabel(self.enames[-1])

        ## SPRITES ##
        self.party = []
        self.comb = []
        self.pointer = makeSprite("images/ppointer.png")
        for i in range(len(self.CHARACTERS)):
            self.party.append(makeSprite(self.CHARACTERS[i].BATTLE_IMAGE))
            moveSprite(self.party[-1], self.charOffsetX + i* 15, (i+1) *30+ self.charOffsetY)
            showSprite(self.party[-1])
        for i in range(len(self.ENEMIES)):
            self.comb.append(makeSprite(self.ENEMIES[i].BATTLE_IMAGE))
            moveSprite(self.comb[-1], 50 - i * 15, (i +1)* 75+self.enemyOffsetY)
            showSprite(self.comb[-1])

        moveSprite(self.pointer, self.party[0].rect.center[0], self.party[0].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
        showSprite(self.pointer)

        ## make adjustable menu screen ##

        ## Main loop ##
        self.inBattle = True
        ## character select ##
        self.prev = None
        self.current = None
        self.charSelect = 0
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
                    playSound(menuBlip, 0)
                    moveSprite(self.pointer, self.party[self.charSelect].rect.center[0], self.party[self.charSelect].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                    changeLabel(self.names[self.charSelect], self.CHARACTERS[self.charSelect].NAME, fontColour= "yellow")
                    changeLabel(self.names[self.charSelect+1], self.CHARACTERS[self.charSelect+1].NAME, fontColour= "white")
                    updateDisplay()
            if self.current == "down":
                if self.charSelect < len(self.party)-1:
                    self.charSelect+=1
                    playSound(menuBlip, 0)
                    moveSprite(self.pointer, self.party[self.charSelect].rect.center[0], self.party[self.charSelect].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                    changeLabel(self.names[self.charSelect], self.CHARACTERS[self.charSelect].NAME, fontColour= "yellow")
                    changeLabel(self.names[self.charSelect-1], self.CHARACTERS[self.charSelect-1].NAME, fontColour= "white")
                    updateDisplay()
            self.turn = self.charSelect # self.current choice

        ## ACTION MENU##

            if self.current == "a":
                for name in self.enames:
                    hideLabel(name)
                    
                self.actions = []
                ## IN MENU ##

                # INITIALIZE MENU TEXT #
                for i in range(len(self.CHARACTERS[i].ACTIONS)):
                    self.actions.append(makeLabel(self.CHARACTERS[self.turn].ACTIONS[i], self.fontSize, 50, (i * 30)+ self.menuOffsetY, "white", font ="fonts/lunchds.ttf", background = 'clear'))
                    showLabel(self.actions[-1])
                changeLabel(self.actions[0], self.CHARACTERS[self.turn].ACTIONS[0], fontColour = "yellow")

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

                            changeLabel(self.actions[self.menuOption], self.CHARACTERS[self.turn].ACTIONS[self.menuOption], fontColour= "yellow")
                            changeLabel(self.actions[self.menuOption+1], self.CHARACTERS[self.turn].ACTIONS[self.menuOption+1], fontColour= "white")
                    elif self.menuInput == "down":
                        if self.menuOption < len(self.actions)-1:
                            self.menuOption+=1

                            changeLabel(self.actions[self.menuOption], self.CHARACTERS[self.turn].ACTIONS[self.menuOption], fontColour= "yellow")
                            changeLabel(self.actions[self.menuOption-1], self.CHARACTERS[self.turn].ACTIONS[self.menuOption-1], fontColour= "white")

                    # PICK ACTION #
                    elif self.menuInput == "a":
                        self.actionDict[self.CHARACTERS[self.turn].ACTIONS[self.menuOption]](self.CHARACTERS[self.turn])
                        self.menuPrev = "b"



                    # CLOSE MENU #
                    elif self.menuInput == "b":
                        for i in range(len(self.actions)):
                            hideLabel(self.actions[i])
                        self.actions = []
                        self.menuOpen = False
                    updateDisplay()
            #end menu loop
                    
            updateDisplay()
            tick(FPS)
            if not self.ENEMIES:
                self.inBattle = False
            #end battle loop
        stopMusic()
        endMusic = makeMusic("sounds/111Fanfare.mp3")
        playMusic()
        endWait()

    def attack(self, char):
        attackPointer = True
        # move pointer to enemy side
        moveSprite(self.pointer, self.comb[0].rect.center[0], self.comb[0].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
        ## character select ##
        attackPrev = "a"
        attackCurrent = None
        attackCharSelect = 0

        for i in self.actions:
            hideLabel(i)
        for i in self.enames:
            showLabel(i)
        changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "yellow")
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

                    moveSprite(self.pointer, self.comb[attackCharSelect].rect.center[0], self.comb[attackCharSelect].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                    changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "yellow")
                    changeLabel(self.enames[attackCharSelect+1], self.ENEMIES[attackCharSelect+1].NAME, fontColour= "white")
            if attackCurrent == "down":
                if attackCharSelect < len(self.comb)-1:
                    attackCharSelect+=1

                    moveSprite(self.pointer, self.comb[attackCharSelect].rect.center[0], self.comb[attackCharSelect].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                    changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "yellow")
                    changeLabel(self.enames[attackCharSelect-1], self.ENEMIES[attackCharSelect-1].NAME, fontColour= "white")

                    
            if attackCurrent == "a":
                ## boy, look at all of this action ##
                self.ENEMIES[attackCharSelect].CURRENT_HEALTH -= char.ATTACK
                changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "white")
                print(self.ENEMIES[attackCharSelect].CURRENT_HEALTH)
                if(self.ENEMIES[attackCharSelect].CURRENT_HEALTH <= 0):
                    hideSprite(self.comb[attackCharSelect])
                    hideLabel(self.enames[attackCharSelect])
                    del self.enames[attackCharSelect]
                    del self.comb[attackCharSelect]
                    del self.ENEMIES[attackCharSelect]
                ## same as press b in menu
                for i in range(len(self.actions)):
                    hideLabel(self.actions[i])
                self.actions = []
                #menu esc
                self.menuOpen = False
                #escape attack
                attackPointer = False
                # move pointer back to original
                moveSprite(self.pointer, self.party[self.turn].rect.center[0], self.party[self.turn].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                
            if attackCurrent == "b":
                changeLabel(self.enames[attackCharSelect], self.ENEMIES[attackCharSelect].NAME, fontColour= "white")
                for i in self.actions:
                    showLabel(i)
                for i in self.enames:
                    hideLabel(i)
                moveSprite(self.pointer, self.party[self.turn].rect.center[0], self.party[self.turn].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
                # go back to action menu
                attackPointer = False
        updateDisplay()


    def defend(self, char):
        ## same as press b in menu
        for i in range(len(self.actions)):
            hideLabel(self.actions[i])
        self.actions = []
        #menu esc
        self.menuOpen = False
        #escape attack
        attackPointer = False
        # move pointer back to original
        moveSprite(self.pointer, self.party[self.turn].rect.center[0], self.party[self.turn].rect.topleft[1]+self.POINTER_BUFFER, centre = True)
        print(char.NAME,"defended")
        return None

enem = ["images/mariorpg_bundt.gif",None, 20, 20, 20, "Cake0", ["Fight", "Defend"]]
data = ["images/starmanMINI.png",None, 10,10,10, "Starman0", ["Fight", "Defend"]]
char = []
combatants = []
for i in range(3):
    char.append(c.CHARACTER(data))
    data[5] = data[5][:-1]+str(i+1)
for i in range(2):
    combatants.append(c.CHARACTER(enem))
    enem[5] = enem[5][:-1]+ str(i+1)
cont = ct.Controller(0)
fight = BATTLE("images/battleBG.png", char, combatants, cont, 600, 600)
