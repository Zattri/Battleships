from tkinter import *
from tkinter import ttk
import Attack, Main, Ai

# Global declarations
labelList = []
coordList = []
buttonDict = {}

# Root declaration
root = Tk()

# Frame declarations
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
framePlace = Frame(root)
frameGrid = Frame(root)
frameMenu = Frame(root)

# [==================================================================================================================]

def fireAttack(x, y):
    # Prints the location of the attack and whether it hit or not
    print("X:",x,"Y:",y, " - ", Attack.checkHit(Main.shipList1, x, y))



def raiseFrame(frame):
    frame.tkraise()


def initFGrid():
    # Adds Column labels to the label list
    for i in range(1, 11):
        labelList.append(ttk.Label(frameGrid, text = i))
        labelList[-1].grid(row = 0, column = i + 1)

    # [MAIN GRID LOOP]
    for row in range(1, 11):
        # Adds Row labels to the label list
        labelList.append(ttk.Label(frameGrid, text = row))
        labelList[-1].grid(row = row + 1, column = 0)

        # [SECONDARY GRID LOOP]
        # Adds buttons for each row top left to bottom right
        for col in range(1, 11):
            loc = str(row) + "," + str(col)
            coordList.append(loc)
            buttonDict[coordList[-1]] = ttk.Button(frameGrid, width = 2)
            buttonDict[coordList[-1]]["command"] = lambda x = col, y = row: fireAttack(x, y)
            buttonDict[coordList[-1]].grid(row = row + 1, column = col + 1)

    # Create a menu button
    Button(frameGrid, text="Menu", command = lambda:raiseFrame(frameMenu)).grid(row = 13, column = 2)
    Button(frameGrid, text="AI", command = lambda:Main.compPlayer.fireShot()).grid(row = 13, column = 4)


def initFMenu():
    Button(frameMenu, text="Attack Grid", command=lambda:raiseFrame(frameGrid)).pack()
    Button(frameMenu, text="Ship Placement", command=lambda:raiseFrame(framePlace)).pack()

def initFPlace():
    # Adds Column labels to the label list
    for i in range(1, 11):
        labelList.append(ttk.Label(framePlace, text = i))
        labelList[-1].grid(row = 0, column = i + 1)

    # [MAIN GRID LOOP]
    for row in range(1, 11):
        # Adds Row labels to the label list
        labelList.append(ttk.Label(framePlace, text = row))
        labelList[-1].grid(row = row + 1, column = 0)

        # [SECONDARY GRID LOOP]
        # Adds buttons for each row top left to bottom right
        for col in range(1, 11):
            loc = str(row) + "," + str(col)
            coordList.append(loc)
            buttonDict[coordList[-1]] = ttk.Button(framePlace, width = 2)
            buttonDict[coordList[-1]]["command"] = lambda x = col, y = row: selectTile(x, y)
            buttonDict[coordList[-1]].grid(row = row + 1, column = col + 1)

    # Directional buttons declaration
    north = Button(framePlace, text = "North").grid(row = 12, column = 6)
    east = Button(framePlace, text="East").grid(row = 13, column = 7)
    west = Button(framePlace, text="West").grid(row = 13, column = 5)
    south = Button(framePlace, text = "South").grid(row = 14, column = 6)

""" #Implement in a bit
def layShipShadow(x, y, orient):
    selectTile(x, y)
    # Get ship length
    lightLen()
"""

def selectTile(x, y):
    button = buttonDict[str(x)+","+str(y)]
    button["bg"] = "yellow"

def clearTiles():
    for i in range(1,11):
        for k in range(1, 11):
            button = buttonDict[str(i)+","+str(k)]
            button.configure(background = "white")

#def lightLen(start, len, orient):


def mainFunc():
    # Set the frames to the base grid, give padding and a title to each frame
    for frame in (f1, f2, f3, f4, frameGrid, frameMenu, framePlace):
        frame.grid(row=0, column=0, sticky='news', padx = 10, pady = 10)
        frame.master.title("Battleships")


    # Initialise all the frames
    initFGrid()
    initFMenu()
    initFPlace()

    """
    #Template for making buttons and labels and attaching them to forms
    Button(f1, text='Go to Grid Frame', command=lambda:raise_frame(frameGrid)).pack()
    Label(f1, text='Grid Frame').pack()
    """

# Runs the main function which declares all the ships and the board etc (for now)
Main.main()
# Main function call inside the GUI class
mainFunc()
# First frame that is loaded
raiseFrame(frameMenu)
root.mainloop()