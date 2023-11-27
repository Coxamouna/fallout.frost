import pygame
from pygame.locals import *
import sys
import colors

FPS = 30
WIDTH = 1024
HEIGHT = 680
IMAGE = "bg.png"
NAME = "Fallout: Frost"
FONT_TYPE = "Fonts\\Overseer Bold.otf"
FONT_SIZE = 69

def main():
    global FPSCLOCK, SCREEN, FONT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    pygame.display.set_caption(NAME)
    BACKGROUND = pygame.image.load(IMAGE)
    SCREEN.blit(BACKGROUND, (0,0))

    FONT = pygame.font.Font(FONT_TYPE, FONT_SIZE) # .Font for custom fonts
    TITLE = FONT.render(NAME, True, colors.IcyGrey)
    SCREEN.blit(TITLE, (WIDTH // 2, 5))
    
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