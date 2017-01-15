import os
# Global file path - Change as needed
filePath = "/users/Zattri/Desktop/"

# The names of all these functions are pretty self-explanatory as to what they do


def closeFile(fileVar):
    if (fileVar != None):
        fileVar.close()
    else:
        print("File is not open or does not exist")


def printFile(filePath, fileName):
    fileVar = open(filePath + fileName, "r")
    print(fileVar.read())


def appendItem(filePath, fileName, newItem):
    fileVar = open(filePath + fileName, "a")
    fileVar.write(newItem+"\n")


def createFile(filePath, fileName, fileTitle = None):
    if (os.path.isfile("./" + fileName) == False):
        fileVar = open(filePath + fileName, "x")
        if (fileTitle != None):
            fileVar.write(fileTitle + "\n")
        return fileVar
    else:
        print("Save file already exists")


def saveFile(team1ships, team2ships):
    if (os.path.isfile(filePath + "/saveState.txt") == False):
        saveVar = createFile(filePath, "saveState.txt")

        # Write in stats for player 1's ships
        saveVar.write("Team 1 Ships\n")
        for ship in team1ships:
            # Retrieve strings of ship info and write to file
            shipStrings = ship.stringStats()
            saveVar.write(shipStrings[0] + "\n")
            saveVar.write(shipStrings[1] + "\n")
            saveVar.write(shipStrings[2] + "\n")

        # Write in stats for player 2's ships
        saveVar.write("Team 2 Ships\n")
        for ship in team2ships:
            # Retrieve strings of ship info and write to file
            shipStrings = ship.stringStats()
            saveVar.write(shipStrings[0] + "\n")
            saveVar.write(shipStrings[1] + "\n")
            saveVar.write(shipStrings[2] + "\n")

        # Close after use
        closeFile(saveVar)

    else:
        print("Save file already exists")

# Do later
def loadFile():
    print("Fix me")

# Open parameters
# r - read
# w - write
# x - create and write
# a - append
# r+ - read and write


