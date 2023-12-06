import pygame
from pygame.locals import *
import colors as color
from menu import Main, Load
import saveload as sl

'''
States:

0 - Game
1 - Main Menu
2 - Load Menu
3 - Pause Menu
4 - Settings Menu
5 - End/Credits Menu
'''

# Game Settings:
FPS = 60
WIDTH = 1024
HEIGHT = 680
NAME = "Fallout: Frost"

class Game:    
    def __init__(self, width, height, name, fps):
        pygame.init()
        self.name = name
        self.width = width
        self.height = height
        self.screen = None
        self.isRunning = True
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.mode = pygame.RESIZABLE
        self.menus = [Main(self.width, self.height, self.fps), Load(self.width, self.height, self.fps)]
        self.state = 1
        self.currentMode = self.menus[0].mode
    
    def inputRouting(self):
        for event in pygame.event.get():
            if (self.state == 0):
                self.state = self.handleInput(event)
            else:
                self.state = self.menus[self.state-1].handleInput(event)

    def handleInput(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return 1
        return 0
    
    def gameIntro(self):
        self.screen.fill(color.NWinterLBlue01)

    def drawGame(self):            
        self.screen.fill(color.NWinterPurple)
        
    def run(self):
        icon = pygame.image.load('Images\\icon.png') 
        pygame.display.set_icon(icon)
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((self.width, self.height), self.currentMode)
        while self.isRunning:
            self.inputRouting()
            if self.state == 0:
                if self.currentMode != self.mode:
                    self.screen = pygame.display.set_mode((self.width, self.height), self.mode)
                    self.currentMode = self.mode
                    if not sl.saveFolderExists(sl.FOLDER): # if the folder DOES NOT exist:
                        sl.createSave()
                        self.gameIntro()
                    else: # if the Saves folder already exists, check if it's empty:
                        saves = sl.saveFileExists(sl.FOLDER, sl.FORMAT)
                        if saves:
                            # self.state == 2 # prompt to Load Menu when Play
                            # self.currentMode = self.menus[1].mode
                            self.drawGame()
                        else: # if the Saves folder is empty:
                            sl.createSave()
                            self.gameIntro()           
            else:
                if self.currentMode != self.menus[self.state-1].mode:
                    self.screen = pygame.display.set_mode((self.width, self.height), self.menus[self.state-1].mode)
                    self.currentMode = self.menus[self.state-1].mode
                self.menus[self.state-1].drawMenu(self.screen)
            pygame.display.update()