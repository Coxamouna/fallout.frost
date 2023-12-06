import pygame
from pygame.locals import *
import colors as color
from menu import Main

# Game Settings:
FPS = 60
WIDTH = 1024
HEIGHT = 680

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
        self.menus = [Main(self.width, self.height, self.fps)]
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
    
    def drawGame(self):            
        self.screen.fill(color.NWinterPurple)
        
    def run(self):
        icon = pygame.image.load('Images\\icon.png') 
        pygame.display.set_icon(icon)
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode((self.width, self.height), self.currentMode)
        while self.isRunning:
            self.inputRouting()
            print(self.state)
            
            if self.state == 0:
                if self.currentMode != self.mode:
                    self.screen = pygame.display.set_mode((self.width, self.height), self.mode)
                    self.currentMode = self.mode
                self.drawGame()
            else:
                if self.currentMode != self.menus[self.state-1].mode:
                    self.screen = pygame.display.set_mode((self.width, self.height), self.menus[self.state-1].mode)
                    self.currentMode = self.menus[self.state-1].mode
                self.menus[self.state-1].drawMenu(self.screen)
            pygame.display.update()
            # TODO: Game drawing
            # self.drawGame()
            # self.clock.tick(self.fps)