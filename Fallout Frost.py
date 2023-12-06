import pygame
from pygame.locals import *
import sys
import colors
import saveload as sm
import game

# Launcher Setup:
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

def main():
    gameRuntime = game.Game(game.WIDTH, game.HEIGHT, NAME, game.FPS)
    gameRuntime.run()

if __name__ == "__main__":
    main()