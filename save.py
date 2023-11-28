import os
from datetime import datetime
from pathlib import Path

FOLDER = "Saves"

def createFile(): # New
    # create the save folder if it doesn't exist or the user deletes it:
    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)
        
    DATE = datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
    SAVE = f"save_{DATE}.txt"

    PATH = os.path.join(FOLDER, SAVE)
    with open(PATH, 'w') as file:
        file.write('Character = "Player"\nGender = Male\nS = 5 \nP = 5\nE = 5\nC = 5\nI = 5\nA = 5\nL = 5\nQuests = 0\nFaction = Vault Dweller\n')

# def loadFile(): # Load
    # check if the folder exists 