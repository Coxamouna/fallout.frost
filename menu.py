import pygame
from pygame.locals import *
import sys
import colors
import gamefiles as gf

# Display Setup:
FPS = 30
WIDTH = 1024
HEIGHT = 680
IMAGE = "Images\\menu.png"
NAME = "Fallout: Frost"

# Title Setup:
TITLE01_NAME = "Fallout:"
TITLE02_NAME = "Frost"
TITLE01_SIZE = 60
TITLE02_SIZE = 80
TITLE_FONT = "Fonts\\Snowinter-Free-For-Personal-Use.otf"

# Menu Setup:
TEXT_SIZE = 18
TEXT_FONT = "Fonts\\jh_fallout-webfont.ttf"
MENU_OPTIONS = ["New", "Load", "Credits", "Quit"]

# Display menu options:
def drawMenu():
    for index, option in enumerate(MENU_OPTIONS):
        TEXT = MENU_FONT.render(option, True, colors.NWinterPink if index == SELECTED_OPTION else colors.NWinterLBlue02)
        TEXTBOX = TEXT.get_rect(center = (WIDTH - 70, HEIGHT // 2 - 90 + index * 50))
        SCREEN.blit(TEXT, TEXTBOX)

# Terminate program:
def terminate():
    pygame.quit()
    sys.exit()

# Menu main function loop:
def main():
    global FPSCLOCK, SCREEN, MENU_FONT, SELECTED_OPTION
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    pygame.display.set_caption(NAME)
    BACKGROUND = pygame.image.load(IMAGE)
    SCREEN.blit(BACKGROUND, (0,0))

    TITLE01_FONT = pygame.font.Font(TITLE_FONT, TITLE01_SIZE) # .Font for custom fonts
    TITLE01 = TITLE01_FONT.render(TITLE01_NAME, True, colors.IcyGrey)
    SCREEN.blit(TITLE01, (6, HEIGHT // 2 - 90))
    
    TITLE02_FONT = pygame.font.Font(TITLE_FONT, TITLE02_SIZE) # .Font for custom fonts
    TITLE02 = TITLE02_FONT.render(TITLE02_NAME, True, colors.IcyGrey)
    SCREEN.blit(TITLE02, (2, HEIGHT // 2 - 50))
    
    MENU_FONT = pygame.font.Font(TEXT_FONT, TEXT_SIZE)
    SELECTED_OPTION = 0
    
    while True: # logic loop
        for event in pygame.event.get():
            if event.type == KEYUP and event.key == K_ESCAPE:
                terminate()
            elif event.type == KEYDOWN and event.key == K_UP :
                SELECTED_OPTION = (SELECTED_OPTION - 1) % len(MENU_OPTIONS)
            elif event.type == KEYDOWN and event.key == K_DOWN:
                SELECTED_OPTION = (SELECTED_OPTION + 1) % len(MENU_OPTIONS)
            elif event.type == KEYDOWN and event.key == K_RETURN:
                    # Perform action based on the selected option:
                    if SELECTED_OPTION == 0:
                        gf.createSave()
                        print("Starting game...")
                        # game.new()
                    elif SELECTED_OPTION == 1:
                        if gf.saveFolderExists(gf.FOLDER):
                            print(f"The folder {gf.FOLDER} exists.")
                            saves = gf.saveFileExists(gf.FOLDER, gf.FORMAT)
                            if saves:
                                print(f"Save files found in {gf.FOLDER}:")
                                for save in saves:
                                    print(save)
                                print("Loading a save file...")
                                # game.load()
                            else:
                                print(f"No save files found in {gf.FOLDER}")
                                gf.createSave()
                                print("Starting game...")
                                # game.new()
                        else:
                            print(f"The folder {gf.FOLDER} does not exist.")
                            # Ask the user if they want to start a New game or go back to the menu
                    elif SELECTED_OPTION == 2:
                        print("Credits...")
                    elif SELECTED_OPTION == 3:
                        print("Exiting the game...")
                        terminate()
        drawMenu()
        pygame.display.flip()              

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
if __name__ == "__main__":
    main()