from Settings import *
from Sprite import *

NumberOfLevels = 5
NumberOfLevels += 1
Moves = 0
class Player(pygame.sprite.Sprite):
    def __init__(self,Tilex,Tiley,Colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TileSize+1,TileSize+1))
        self.image.fill(Colour)
        self.rect = self.image.get_rect()
        self.Tilex = Tilex
        self.Tiley = Tiley
        self.x = (Tilex*TileSize)+(TileSize/2)
        self.y = (Tiley*TileSize)+(TileSize/2)
        self.dX = 0
        self.dY = 0
        self.rect.center=((self.x,self.y))
        self.carry = False
        self.add(AllSprites)
        self.add(Players)
    def update(self):
        self.x = (self.Tilex*TileSize)+(TileSize/2)
        self.y = (self.Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))

    def CollideWithWalls(self):
        for Wall in Walls:
            if Wall.Tilex == self.Tilex + self.dX and Wall.Tiley == self.Tiley + self.dY:
                return True
        for Wall in ButtonWalls:
             if Wall.Tilex == self.Tilex + self.dX and Wall.Tiley == self.Tiley + self.dY:
                 return True
        if self.Tilex + self.dX < 0:
            return True
        elif self.Tilex + self.dX > 31:
            return True
        if self.Tiley + self.dY < 0:
            return True
        elif self.Tiley + self.dY > 23:
            return True
        return False
    def CollideWithButton(self):
        for Button in Buttons:
             if Button.Tilex == self.Tilex + self.dX and Button.Tiley == self.Tiley + self.dY:
                     for sprite in Button.group:
                         sprite.remove(ButtonWalls)
             if Button.Tilex == self.Tilex and Button.Tiley == self.Tiley :
                  if Button.Colour == GREEN:
                      for sprite in GreenWalls:
                              sprite.add(ButtonWalls)
                  else:
                      for sprite in PurpleWalls:
                          sprite.add(ButtonWalls)
    def CollideWithFlag(self):
        for flag in Flags:
            if flag.Tilex == self.Tilex + self.dX and flag.Tiley == self.Tiley + self.dY:
                flag.carry = True
                self.carry = True

    def CollideWithObject(self):
        for ob in Objectives:
            if ob.Tilex == self.Tilex and ob.Tiley == self.Tiley and self.carry == True:
                global Run
                Run = False
    def Move(self,Direction):
        if Direction == "Up":
            self.dY = -1
        elif Direction == "Down":
            self.dY = 1
        else:
            self.dY = 0

        if Direction == "Right":
            self.dX = 1
        elif Direction == "Left":
            self.dX = -1
        else:
            self.dX = 0
        self.CollideWithFlag()
        self.CollideWithButton()
        if self.CollideWithWalls() == False:
            self.Tilex += self.dX
            self.Tiley += self.dY
        self.CollideWithObject()
    def HandOverSelf(self):
        if self.carry == True:
            self.carry = False
        else:
            self.carry = True

def PlayerMove(key,Player1,Player2):
    global Moves
    if (key == pygame.K_ESCAPE):
        Quit()
    elif (key == pygame.K_SPACE):
        HandOver()
    elif (key == pygame.K_r):
        global Run
        Run = False
    else:
        Moves += 1
        if (key == pygame.K_a):
            Player1.Move("Left")
        if (key == pygame.K_d):
            Player1.Move("Right")
        if (key == pygame.K_w):
            Player1.Move("Up")
        if (key == pygame.K_s):
            Player1.Move("Down")
        if (key == pygame.K_LEFT):
            Player2.Move("Left")
        if (key == pygame.K_RIGHT):
            Player2.Move("Right")
        if (key == pygame.K_UP):
            Player2.Move("Up")
        if (key == pygame.K_DOWN):
            Player2.Move("Down")
        if (key == pygame.K_q):
            Quit()

def GameLoop():
    NextLevel()
    global Level
    Player1 = Player(Player1Spawn[(Level*2)-2],Player1Spawn[(Level*2)-1],YELLOW)
    Player2 = Player(Player2Spawn[(Level*2)-2],Player2Spawn[(Level*2)-1],BLUE)
    global Run
    Run = True
    pygame.key.set_repeat(100,100) #Before starting How often
    while Run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Quit()
            elif (e.type == pygame.KEYDOWN):
                PlayerMove(e.key,Player1,Player2)
        ScreenBlit(GameDisplay)

for i in range(1,NumberOfLevels):
    GameLoop()

EndTimer = time.time()-StartTime
EndTimer = int(EndTimer)
print(EndTime(EndTimer))
print(Moves)
