from Settings import *
Level = 0
Run = True



class UnPassable(pygame.sprite.Sprite):
    def __init__(self,Tilex,Tiley):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TileSize+1,TileSize+1))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.Tilex = Tilex
        self.Tiley = Tiley
        self.x = (Tilex*TileSize)+(TileSize/2)
        self.y = (Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
        self.add(Walls)
        self.add(AllSprites)
    def update(self):
        self.x = (self.Tilex*TileSize)+(TileSize/2)
        self.y = (self.Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
class Objective(pygame.sprite.Sprite):
    def __init__(self,Tilex,Tiley):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TileSize+1,TileSize+1))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.Tilex = Tilex
        self.Tiley = Tiley
        self.x = (Tilex*TileSize)+(TileSize/2)
        self.y = (Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
        self.add(Objectives)
        self.add(AllSprites)
    def update(self):
        self.x = (self.Tilex*TileSize)+(TileSize/2)
        self.y = (self.Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
class FlagCarry(pygame.sprite.Sprite):
    def __init__(self,Tilex,Tiley):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((int(TileSize/2),int(TileSize/2)))
        self.image.fill(FLAGCOLOUR)
        self.rect = self.image.get_rect()
        self.Tilex = Tilex
        self.Tiley = Tiley
        self.x = (Tilex*TileSize)+(TileSize/2)
        self.y = (Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
        self.carry = False
        self.add(AllSprites)
        self.add(Flags)
    def update(self):
        if self.carry == True:
            for player in Players:
                if player.carry == True:
                    self.Tilex = player.Tilex
                    self.Tiley = player.Tiley
        self.x = (self.Tilex*TileSize)+(TileSize/2)
        self.y = (self.Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
class Button(pygame.sprite.Sprite):
    def __init__(self,Tilex,Tiley,Colour,C):
        pygame.sprite.Sprite.__init__(self)
        self.Colour = Colour
        if Colour == GREEN:
            self.group = GreenWalls
        else:
            self.group = PurpleWalls
        self.image = pygame.Surface((TileSize+1,TileSize+1))
        self.image.fill(C)
        self.rect = self.image.get_rect()
        self.Tilex = Tilex
        self.Tiley = Tiley
        self.x = (Tilex*TileSize)+(TileSize/2)
        self.y = (Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
        self.down = False
        self.add(Buttons)
        self.add(AllSprites)
    def update(self):
        self.x = (self.Tilex*TileSize)+(TileSize/2)
        self.y = (self.Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
class ColouredWalls(pygame.sprite.Sprite):
    def __init__(self,Tilex,Tiley,Colour):
        pygame.sprite.Sprite.__init__(self)
        self.Colour = Colour
        self.image = pygame.Surface((TileSize+1,TileSize+1))
        self.image.fill(Colour)
        self.rect = self.image.get_rect()
        self.Tilex = Tilex
        self.Tiley = Tiley
        self.x = (Tilex*TileSize)+(TileSize/2)
        self.y = (Tiley*TileSize)+(TileSize/2)
        self.rect.center=((self.x,self.y))
        self.Visable = True
        if Colour == GREEN:
            self.add(GreenWalls)
        else:
            self.add(PurpleWalls)
        self.add(AllSprites)
        self.add(ButtonWalls)
    def update(self):
        if self.Visable == True:
            self.x = (self.Tilex*TileSize)+(TileSize/2)
            self.y = (self.Tiley*TileSize)+(TileSize/2)
            self.rect.center=((self.x,self.y))
        else:
            self.x = (self.Tilex*TileSize)+(TileSize/2)+DisplayWidth
            self.y = (self.Tiley*TileSize)+(TileSize/2)+DisplayHeight
            self.rect.center=((self.x,self.y))

def SpawnBaseLevel(Level):
    MapData = []
    GameFolder = os.path.dirname(__file__)
    with open(os.path.join(GameFolder, "Level"+str(Level)+".txt"), 'r') as file:
        for line in file:
            line = line.strip("\n")
            MapData.append(line)
    return MapData
def MapCreate(Data):
    for col, tiles in enumerate(Data):
        for row, tile in enumerate(tiles):
            if tile == '0':
                UnPassable(row,col)
            elif tile == "1":
                Player1Spawn.append(row)
                Player1Spawn.append(col)
            elif tile == "2":
                Player2Spawn.append(row)
                Player2Spawn.append(col)
            elif tile == "F":
                Flag = FlagCarry(row,col)
            elif tile == "O":
                Objective(row,col)
            elif tile == "G":
                ColouredWalls(row,col,GREEN)
            elif tile == "H":
                Button(row,col,GREEN,BUTGREEN)
            elif tile == "I":
                ColouredWalls(row,col,PURPLE)
            elif tile == "P":
                Button(row,col,PURPLE,BUTPURPLE)

def HandOver():
    for player in Players:
        player.HandOverSelf()
def DropFlag():
    for f in Flags:
        f.carry = False
    for p in Players:
        p.carry = False
def NextLevel():
    global Level
    Level += 1
    Player1Spawn = []
    Player2Spawn = []
    for s in AllSprites:
        s.kill()
    MapCreate(SpawnBaseLevel(Level))
