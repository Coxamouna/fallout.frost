import os
import re
from datetime import datetime

FOLDER = "Saves"
FORMAT = r"save_\d{8}__\d{6}\.txt"

def createFolder(): # New/Load
    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)

def createSave(): # New
    createFolder()
    SAVE = f"save_{datetime.now().strftime('%d%m%Y__%H%M%S')}.txt"

    PATH = os.path.join(FOLDER, SAVE)
    with open(PATH, 'w') as file:
        file.write('Character = "Player"\nGender = Male\nS = 5 \nP = 5\nE = 5\nC = 5\nI = 5\nA = 5\nL = 5\nQuests = 0\nFaction = Vault Dweller\n')

def saveFileExists(FOLDER, FORMAT): # Load
    list = os.listdir(FOLDER)
    # Create a regex pattern based on the provided pattern:
    pattern = re.compile(FORMAT)
    # Check if any file matches the pattern:
    matches = [file for file in list if pattern.match(file)]
    
    return matches

def saveFolderExists(FOLDER): # Load
    return os.path.exists(FOLDER) and os.path.isdir(FOLDER)
    
# def loadSave(): # Load