import pygame
from pygame.locals import *
import sys
import colors

FPS = 30
WIDTH = 1024
HEIGHT = 680
IMAGE = "bg.png"
NAME = "Fallout: Frost"

TITLE01_NAME = "Fallout:"
TITLE01_SIZE = 50
TITLE02_NAME = "Frost"
TITLE02_SIZE = 70
FONT_TYPE = "Fonts\\Snowinter-Free-For-Personal-Use.otf"

def main():
    global FPSCLOCK, SCREEN, FONT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    pygame.display.set_caption(NAME)
    BACKGROUND = pygame.image.load(IMAGE)
    SCREEN.blit(BACKGROUND, (0,0))

    TITLE01_FONT = pygame.font.Font(FONT_TYPE, TITLE01_SIZE) # .Font for custom fonts
    TITLE01 = TITLE01_FONT.render(TITLE01_NAME, True, colors.IcyGrey)
    SCREEN.blit(TITLE01, (6, HEIGHT // 2))
    
    TITLE02_FONT = pygame.font.Font(FONT_TYPE, TITLE02_SIZE) # .Font for custom fonts
    TITLE02 = TITLE02_FONT.render(TITLE02_NAME, True, colors.IcyGrey)
    SCREEN.blit(TITLE02, (2, HEIGHT // 2 + 30))
    
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                terminate()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()   
    sys.exit()

if __name__ == "__main__":
    main()