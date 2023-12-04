import pygame
from pygame.locals import *
import sys
import colors as color
import saveload as sl
import sys

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
            super().__init__(width, height, fps, BACKGROUND, MENU_OPTIONS)
    
    def handleInput(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: # for starters:
                self.terminate()
            elif event.key == K_UP :
                self.selection = (self.selection - 1) % len(self.options)
            elif event.key == K_DOWN:
                self.selection = (self.selection + 1) % len(self.options)
            elif event.key == K_RETURN:
                if self.selection == 0: # Play
                    if not sl.saveFolderExists(sl.FOLDER):
                        print(f"The folder {sl.FOLDER} DOES NOT exist!")
                        print(f"Creating {sl.FOLDER}/save__date__time.txt:")
                        sl.createSave()
                        print("Starting save file...")
                        return 0 # Game State
                    else: 
                        print(f"The folder {sl.FOLDER} exists!")
                        saves = sl.saveFileExists(sl.FOLDER, sl.FORMAT)
                        if saves:
                            print(f"Save files found in {sl.FOLDER}!")
                            return 0 # 2 # Load State
                            # for save in saves:
                            #     print(save)
                        else:
                            print(f"The folder {sl.FOLDER} is empty.")
                            print(f"Creating save__date__time.txt in {sl.FOLDER}:")
                            sl.createSave()
                            print("Starting save file...")
                            return 0 # Game State
                elif self.selection == 1: # Options/Credits:
                    print("Credits/Options...")
                    pass
                elif self.selection == 3: # Exit
                    print("Exiting the game...")
                    self.terminate()       
        return 1
     
# class Load(Menu):
#     def __init__(self, width, height, fps, background, options):
# class Options/Credits(Menu):
#     def __init__(self, width, height, fps, background, options):
# class Pause(Menu):
#     def __init__(self, width, height, fps, background, options):

# Menu SETTINGS:
WIDTH = 1024
HEIGHT = 680
FPS = 30
BACKGROUND = "Images\\menu.png"
MENU_OPTIONS = ["Play", "Credits", "Exit"]
SAVES_OPTIONS = ["save1", "save2", "save3"] # ????
LOAD_OPTIONS = ["New", "Load", "Return"] # Return to the SAVES_OPTIONS
PAUSE_OPTIONS = ["Resume", "Quit"]