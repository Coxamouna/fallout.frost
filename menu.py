import pygame
from pygame.locals import *
import sys
import colors as color
import sys

# Menu SETTINGS:
WIDTH = 1024
HEIGHT = 680
FPS = 30
BACKGROUND = "Images\\menu.png"
MAIN_OPTIONS = ["Play", "Options", "Exit"]
LOAD_OPTIONS = ["New", "Load", "Return"] # Return to the SAVES_OPTIONS
    # SAVES_OPTIONS = ["save1", "save2", "save3"]
PAUSE_OPTIONS = ["Resume", "Quit"]
SETTINGS_OPTIONS = []
CREDITS_OPTIONS = []

# Title Setup:
TITLE01_NAME = "Fallout:"
TITLE02_NAME = "Frost"
TITLE01_SIZE = 60
TITLE02_SIZE = 80
TITLE_FONT = "Fonts\\Snowinter-Free-For-Personal-Use.otf"

class Menu:
    NAME = "Fallout : Frost"
    def __init__(self, width, height, fps, background, options):
        self.width = width
        self.height = height
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.textFont = "Fonts\\jh_fallout-webfont.ttf"
        self.textSize = 18
        self.menuFont = pygame.font.Font(self.textFont, self.textSize)
        self.background = background
        self.options = options
        self.selection = 0 # first selection
        self.mode = pygame.NOFRAME
    
    def drawMenu(self, screen):
        self.background = pygame.image.load(BACKGROUND)
        screen.blit(self.background, (0,0))
        for index, option in enumerate(self.options):
            TEXT = self.menuFont.render(option, True, color.NWinterPink if index == self.selection else color.NWinterLBlue02)
            TEXTBOX = TEXT.get_rect(center = (self.width - 70, self.height // 2 - 90 + index * 50))
            screen.blit(TEXT, TEXTBOX)
    
    def handleInput(self, event):
        pass
                
    def windowChange(self):
        pygame.display.set_caption(self.NAME)
        self.screen = pygame.display.set_mode((self.width, self.height), self.mode)
                
    def terminate(self):
        pygame.quit()
        sys.exit()

class Main(Menu):
    def __init__(self, width, height, fps):
            super().__init__(width, height, fps, BACKGROUND, MAIN_OPTIONS)
    
    def drawMenu(self, screen):
        super().drawMenu(screen)
        TITLE01_FONT = pygame.font.Font(TITLE_FONT, TITLE01_SIZE)
        TITLE01 = TITLE01_FONT.render(TITLE01_NAME, True, color.IcyGrey)
        screen.blit(TITLE01, (6, HEIGHT // 2 - 90))
    
        TITLE02_FONT = pygame.font.Font(TITLE_FONT, TITLE02_SIZE) # .Font for custom fonts
        TITLE02 = TITLE02_FONT.render(TITLE02_NAME, True, color.IcyGrey)
        screen.blit(TITLE02, (2, HEIGHT // 2 - 50))
    
    def handleInput(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: # for starters:
                self.terminate()
            elif event.key == K_UP :
                self.selection = (self.selection - 1) % len(self.options)
            elif event.key == K_DOWN:
                self.selection = (self.selection + 1) % len(self.options)
            elif event.key == K_RETURN:
                if self.selection == 0: # Play - Game = 0
                    return 0
                elif self.selection == 1: # Options
                    print("Credits/Options...")
                    pass
                elif self.selection == 3: # Exit
                    print("Exiting the game...")
                    self.terminate()       
        return 1
     
class Load(Menu):
    def __init__(self, width, height, fps):
        super().__init__(width, height, fps, BACKGROUND, LOAD_OPTIONS)
    
    def handleInput(self, event):
        pass

class Pause(Menu):
    def __init__(self, width, height, fps):
        super().__init__(width, height, fps, BACKGROUND, PAUSE_OPTIONS)
     
    def handleInput(self, event):
        pass
    
class Settings(Menu):
    def __init__(self, width, height, fps):
        super().__init__(width, height, fps, BACKGROUND, SETTINGS_OPTIONS)
     
    def handleInput(self, event):
        pass
    
class Credits(Menu):
    def __init__(self, width, height, fps):
        super().__init__(width, height, fps, BACKGROUND, CREDITS_OPTIONS)
     
    def handleInput(self, event):
        pass 