import pygame
import sys
import os
import time

DisplayWidth = 1025 # 16 * 64 or 32 * 32
DisplayHeight = 769 # 16 * 48 or 32 * 24
TilesWide = 32
TilesTall = 24
TileSize = int(DisplayWidth/TilesWide)
RED = (255,0,0)
FLAGCOLOUR = (180,10,10)
YELLOW = (255,255,51)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (180,180,180)
BLUE = (25,30,255)
GREEN = (10,200,10)
BUTGREEN=(5,150,5)
PURPLE = (155,0,155)
BUTPURPLE = (100,0,100)

GridColour = GREY
BgColour = BLACK

AllSprites = pygame.sprite.Group()
Players = pygame.sprite.Group()
Walls = pygame.sprite.Group()
Flags = pygame.sprite.Group()
Objectives = pygame.sprite.Group()
Buttons = pygame.sprite.Group()
GreenWalls = pygame.sprite.Group()
PurpleWalls = pygame.sprite.Group()
ButtonWalls = pygame.sprite.Group()
StartTime = time.time()

GameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight),pygame.FULLSCREEN)
#,pygame.FULLSCREEN
Player1Spawn = []
Player2Spawn = []



Clock = pygame.time.Clock()


def SpritesDraw(self):
    Walls.update()
    Walls.draw(self)
    Objectives.update()
    Objectives.draw(self)
    Buttons.update()
    Buttons.draw(self)
    Players.update()
    Players.draw(self)
    Flags.update()
    Flags.draw(self)
    ButtonWalls.update()
    ButtonWalls.draw(self)


def BackgroundDraw(Display,Spacing,SpaceColour,BackgroundColour):
    GameDisplay.fill(BackgroundColour)
    for x in range(0, DisplayWidth, Spacing):
        pygame.draw.line(Display, SpaceColour, (x, 0),(x, DisplayHeight))
    for y in range(0, DisplayHeight, Spacing):
        pygame.draw.line(Display, SpaceColour,(0, y),(DisplayWidth,y))

def ScreenBlit(Screen):
    BackgroundDraw(Screen,TileSize,GridColour,BgColour)
    SpritesDraw(Screen)
    pygame.display.update()

def Quit():
    pygame.quit()
    sys.exit()
    os.quit()
    

def EndTime(TimeTaken):
    EndMinutes = 0
    EndSeconds = 0
    while TimeTaken > 60:
        EndMinutes += 1
        TimeTaken -= 60
    EndSeconds = TimeTaken
    return EndMinutes, EndSeconds
