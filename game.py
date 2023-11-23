import pygame
from pygame.locals import *
import sys

WINDOWWIDTH = 0
WINDOWHEIGHT = 0

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.RESIZABLE)
BACKGROUND = pygame.image.load("dweller.png")

pygame.display.set_caption("Fallout '24")
while True:
    DISPLAYSURF.blit(BACKGROUND, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    pygame.display.update()