from tkinter import *
from tkinter import ttk
from fileFuncts import saveFile
from random import randint
from time import sleep
from sys import stdout
import Attack, Main



# Global declarations
labelList = []
coordList = []
divisionList = []
buttonDict = {}
boardSize = 8

# Root declaration
root = Tk()

# Frame declarations
frameGrid1 = Frame(root)
frameMenu = Frame(root)


# [==================================================================================================================]

def fireAttack(button, x, y, shipList):
    global turnLabel
    global attackLabel
    if (Attack.checkHit(shipList, x, y) == True):
        changeColour(button, "red")
        attackLabel["text"] = "Attack Again!"
    else:
        changeColour(button, "grey")
        if shipList == Main.shipList1:
            turnLabel["text"] = "Player 2's turn"
            attackLabel["text"] = ""
        else:
            turnLabel["text"] = "Player 1's turn"
            attackLabel["text"] = ""

# Computer attack function
def compAttack(colList):
    # Computer "Thinking" time - This shouldn't be an objective please remove it, it's too easy to implement,
    # pointless and slows the game down so much.
    stdout.write("Thinking")
    stdout.flush()
    sleep(0.5)
    stdout.write(".")
    stdout.flush()
    sleep(0.5)
    stdout.write(".")
    stdout.flush()
    sleep(0.5)
    stdout.write(".")
    stdout.flush()
    sleep(0.5)
    print(" Done")

    allowAttack = False
    # Repeat the attack until an un-targeted square is selected
    while allowAttack == False:
        global randXPos
        global randYPos
        global attackButton
        randXPos = randint(1, boardSize)
        randYPos = randint(1, boardSize)

        atkColList = colList[randXPos-1]
        attackButton = atkColList[randYPos-1]
        # Allow the attack if the square has not been targeted before
        if (attackButton["bg"] == "blue"):
            allowAttack = True
            fireAttack(attackButton, randYPos, randXPos, Main.shipList2)

    if attackButton["bg"] == "red":
        print("Computer hit, attacking again!")
        compAttack(colList)


# Raises the chosen frame
def raiseFrame(frame):
    frame.tkraise()


# Changing colour doesn't work
def changeColour(button, colour):
    button["bg"] = str(colour)


# Alters the size of the board
def changeBoardSize(value):
    global boardSize
    boardSize = value
    print("Board size changed to",boardSize)


# Start game procedure that raises the battlegrid frame
def startGame():
    initBattleGrid1()
    raiseFrame(frameGrid1)


# Create the menu frame
def initMenu():
    Button(frameMenu, text="Start Game", width=15, height=5, command=lambda:startGame()).pack()
    Button(frameMenu, text="Size 8", width=15, height=5, command=lambda:changeBoardSize(8)).pack()
    Button(frameMenu, text="Size 10", width=15, height=5, command=lambda:changeBoardSize(10)).pack()


# Defines main running function for GUI
def mainFunc():
    # Initialise the battlegrid frame
    frameGrid1.grid(row=0, column=0, sticky='news', padx = 10, pady = 10)
    frameGrid1.master.title("Battleships")

    # Initialise menu frame
    frameMenu.grid(row=0, column=0, sticky='news', padx = 100, pady = 50)
    frameMenu.master.title("Battleships")
    initMenu()


# Define the battlegrid frame
def initBattleGrid1():
    # Declare global variables so they can be used in other functions to change turns
    global turnLabel
    global attackLabel

    # Adds menu buttons and an AI fire button
    Button(frameGrid1, text="Menu", command=lambda: raiseFrame(frameMenu)).grid(row=13, column=23)
    Button(frameGrid1, text="AI", command=lambda: compAttack(p2colsList)).grid(row=14, column=23)
    Button(frameGrid1, text="Save Game", command=lambda: saveFile(Main.shipList1, Main.shipList2)).grid(row=15, column=23)

    # Turn label to indicate who's turn it is
    turnLabel = Label(frameGrid1, text="Player 1\'s turn")
    turnLabel.grid(row=4, column=24)

    # Label to indicate whether a player should attack again
    attackLabel = Label(frameGrid1, text="")
    attackLabel.grid(row=5, column=24)

    # Adds division labels
    for i in range(1,boardSize+1):
        divisionList.append(ttk.Label(frameGrid1, text=" ", width=3))
        divisionList[-1].grid(row=i, column=11)

    # Adds Column labels to the label list
    for col in range(1, boardSize+1):
        labelList.append(ttk.Label(frameGrid1, text=col))
        labelList[-1].grid(row=0, column=col)

        # 2nd grid labels
        labelList.append(ttk.Label(frameGrid1, text=col))
        labelList[-1].grid(row=0, column=col+11)

    # rowStrList lists the strings of each row for naming purposes
    # If checks that size of the board and alters the labels accordingly
    if (boardSize == 8):
        rowStrList = ["A", "B", "C", "D", "E", "F", "G", "H"]
    else:
        rowStrList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    # Adds Row labels to the label list
    for row in rowStrList:
        # Adds Row labels to the label list
        labelList.append(ttk.Label(frameGrid1, text=row))
        labelList[-1].grid(row=rowStrList.index(row) + 1, column=0)

        # 2nd grid labels
        labelList.append(ttk.Label(frameGrid1, text=row))
        labelList[-1].grid(row=rowStrList.index(row) + 1, column=22)

    # Declaration for buttons in Row A
    A1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A1, 1, 1, Main.shipList1))
    A2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A2, 2, 1, Main.shipList1))
    A3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A3, 3, 1, Main.shipList1))
    A4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A4, 4, 1, Main.shipList1))
    A5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A5, 5, 1, Main.shipList1))
    A6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A6, 6, 1, Main.shipList1))
    A7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A7, 7, 1, Main.shipList1))
    A8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A8, 8, 1, Main.shipList1))
    A9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A9, 9, 1, Main.shipList1))
    A10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(A10, 10, 1, Main.shipList1))
    # Add buttons to column list
    colA = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10]

    B1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B1, 1, 2, Main.shipList1))
    B2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B2, 2, 2, Main.shipList1))
    B3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B3, 3, 2, Main.shipList1))
    B4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B4, 4, 2, Main.shipList1))
    B5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B5, 5, 2, Main.shipList1))
    B6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B6, 6, 2, Main.shipList1))
    B7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B7, 7, 2, Main.shipList1))
    B8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B8, 8, 2, Main.shipList1))
    B9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B9, 9, 2, Main.shipList1))
    B10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(B10, 10, 2, Main.shipList1))
    colB = [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10]

    C1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C1, 1, 3, Main.shipList1))
    C2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C2, 2, 3, Main.shipList1))
    C3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C3, 3, 3, Main.shipList1))
    C4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C4, 4, 3, Main.shipList1))
    C5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C5, 5, 3, Main.shipList1))
    C6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C6, 6, 3, Main.shipList1))
    C7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C7, 7, 3, Main.shipList1))
    C8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C8, 8, 3, Main.shipList1))
    C9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C9, 9, 3, Main.shipList1))
    C10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(C10, 10, 3, Main.shipList1))
    colC = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10]

    D1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D1, 1, 4, Main.shipList1))
    D2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D2, 2, 4, Main.shipList1))
    D3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D3, 3, 4, Main.shipList1))
    D4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D4, 4, 4, Main.shipList1))
    D5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D5, 5, 4, Main.shipList1))
    D6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D6, 6, 4, Main.shipList1))
    D7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D7, 7, 4, Main.shipList1))
    D8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D8, 8, 4, Main.shipList1))
    D9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D9, 9, 4, Main.shipList1))
    D10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(D10, 10, 4, Main.shipList1))
    colD = [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10]

    E1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E1, 1, 5, Main.shipList1))
    E2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E2, 2, 5, Main.shipList1))
    E3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E3, 3, 5, Main.shipList1))
    E4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E4, 4, 5, Main.shipList1))
    E5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E5, 5, 5, Main.shipList1))
    E6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E6, 6, 5, Main.shipList1))
    E7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E7, 7, 5, Main.shipList1))
    E8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E8, 8, 5, Main.shipList1))
    E9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E9, 9, 5, Main.shipList1))
    E10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(E10, 10, 5, Main.shipList1))
    colE = [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10]

    F1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F1, 1, 6, Main.shipList1))
    F2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F2, 2, 6, Main.shipList1))
    F3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F3, 3, 6, Main.shipList1))
    F4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F4, 4, 6, Main.shipList1))
    F5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F5, 5, 6, Main.shipList1))
    F6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F6, 6, 6, Main.shipList1))
    F7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F7, 7, 6, Main.shipList1))
    F8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F8, 8, 6, Main.shipList1))
    F9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F9, 9, 6, Main.shipList1))
    F10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(F10, 10, 6, Main.shipList1))
    colF = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10]

    G1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G1, 1, 7, Main.shipList1))
    G2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G2, 2, 7, Main.shipList1))
    G3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G3, 3, 7, Main.shipList1))
    G4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G4, 4, 7, Main.shipList1))
    G5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G5, 5, 7, Main.shipList1))
    G6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G6, 6, 7, Main.shipList1))
    G7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G7, 7, 7, Main.shipList1))
    G8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G8, 8, 7, Main.shipList1))
    G9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G9, 9, 7, Main.shipList1))
    G10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(G10, 10, 7, Main.shipList1))
    colG = [G1, G2, G3, G4, G5, G6, G7, G8, G9, G10]

    H1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H1, 1, 8, Main.shipList1))
    H2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H2, 2, 8, Main.shipList1))
    H3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H3, 3, 8, Main.shipList1))
    H4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H4, 4, 8, Main.shipList1))
    H5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H5, 5, 8, Main.shipList1))
    H6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H6, 6, 8, Main.shipList1))
    H7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H7, 7, 8, Main.shipList1))
    H8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H8, 8, 8, Main.shipList1))
    H9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H9, 9, 8, Main.shipList1))
    H10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(H10, 10, 8, Main.shipList1))
    colH = [H1, H2, H3, H4, H5, H6, H7, H8, H9, H10]

    I1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I1, 1, 9, Main.shipList1))
    I2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I2, 2, 9, Main.shipList1))
    I3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I3, 3, 9, Main.shipList1))
    I4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I4, 4, 9, Main.shipList1))
    I5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I5, 5, 9, Main.shipList1))
    I6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I6, 6, 9, Main.shipList1))
    I7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I7, 7, 9, Main.shipList1))
    I8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I8, 8, 9, Main.shipList1))
    I9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I9, 9, 9, Main.shipList1))
    I10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(I10, 10, 9, Main.shipList1))
    colI = [I1, I2, I3, I4, I5, I6, I7, I8, I9, I10]

    J1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J1, 1, 10, Main.shipList1))
    J2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J2, 2, 10, Main.shipList1))
    J3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J3, 3, 10, Main.shipList1))
    J4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J4, 4, 10, Main.shipList1))
    J5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J5, 5, 10, Main.shipList1))
    J6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J6, 6, 10, Main.shipList1))
    J7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J7, 7, 10, Main.shipList1))
    J8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J8, 8, 10, Main.shipList1))
    J9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J9, 9, 10, Main.shipList1))
    J10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(J10, 10, 10, Main.shipList1))
    colJ = [J1, J2, J3, J4, J5, J6, J7, J8, J9, J10]

    # Set the board to use the correct amount of buttons
    if (boardSize == 8):
        colA = [A1, A2, A3, A4, A5, A6, A7, A8]
        colB = [B1, B2, B3, B4, B5, B6, B7, B8]
        colC = [C1, C2, C3, C4, C5, C6, C7, C8]
        colD = [D1, D2, D3, D4, D5, D6, D7, D8]
        colE = [E1, E2, E3, E4, E5, E6, E7, E8]
        colF = [F1, F2, F3, F4, F5, F6, F7, F8]
        colG = [G1, G2, G3, G4, G5, G6, G7, G8]
        colH = [H1, H2, H3, H4, H5, H6, H7, H8]
        colsList = [colA, colB, colC, colD, colE, colF, colG, colH]

    else:
        colsList = [colA, colB, colC, colD, colE, colF, colG, colH, colI, colJ]

    for cols in colsList:
        for button in cols:
            button.grid(row=colsList.index(cols)+1, column=cols.index(button)+1)



    # Declaration for second grid
    p2A1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A1, 1, 1, Main.shipList2))
    p2A2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A2, 2, 1, Main.shipList2))
    p2A3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A3, 3, 1, Main.shipList2))
    p2A4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A4, 4, 1, Main.shipList2))
    p2A5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A5, 5, 1, Main.shipList2))
    p2A6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A6, 6, 1, Main.shipList2))
    p2A7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A7, 7, 1, Main.shipList2))
    p2A8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A8, 8, 1, Main.shipList2))
    p2A9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A9, 9, 1, Main.shipList2))
    p2A10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2A10, 10, 1, Main.shipList2))
    p2colA = [p2A1, p2A2, p2A3, p2A4, p2A5, p2A6, p2A7, p2A8, p2A9, p2A10]

    p2B1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B1, 1, 2, Main.shipList2))
    p2B2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B2, 2, 2, Main.shipList2))
    p2B3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B3, 3, 2, Main.shipList2))
    p2B4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B4, 4, 2, Main.shipList2))
    p2B5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B5, 5, 2, Main.shipList2))
    p2B6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B6, 6, 2, Main.shipList2))
    p2B7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B7, 7, 2, Main.shipList2))
    p2B8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B8, 8, 2, Main.shipList2))
    p2B9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B9, 9, 2, Main.shipList2))
    p2B10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2B10, 10, 2, Main.shipList2))
    p2colB = [p2B1, p2B2, p2B3, p2B4, p2B5, p2B6, p2B7, p2B8, p2B9, p2B10]

    p2C1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C1, 1, 3, Main.shipList2))
    p2C2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C2, 2, 3, Main.shipList2))
    p2C3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C3, 3, 3, Main.shipList2))
    p2C4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C4, 4, 3, Main.shipList2))
    p2C5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C5, 5, 3, Main.shipList2))
    p2C6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C6, 6, 3, Main.shipList2))
    p2C7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C7, 7, 3, Main.shipList2))
    p2C8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C8, 8, 3, Main.shipList2))
    p2C9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C9, 9, 3, Main.shipList2))
    p2C10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2C10, 10, 3, Main.shipList2))
    p2colC = [p2C1, p2C2, p2C3, p2C4, p2C5, p2C6, p2C7, p2C8, p2C9, p2C10]

    p2D1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D1, 1, 4, Main.shipList2))
    p2D2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D2, 2, 4, Main.shipList2))
    p2D3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D3, 3, 4, Main.shipList2))
    p2D4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D4, 4, 4, Main.shipList2))
    p2D5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D5, 5, 4, Main.shipList2))
    p2D6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D6, 6, 4, Main.shipList2))
    p2D7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D7, 7, 4, Main.shipList2))
    p2D8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D8, 8, 4, Main.shipList2))
    p2D9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D9, 9, 4, Main.shipList2))
    p2D10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2D10, 10, 4, Main.shipList2))
    p2colD = [p2D1, p2D2, p2D3, p2D4, p2D5, p2D6, p2D7, p2D8, p2D9, p2D10]

    p2E1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E1, 1, 5, Main.shipList2))
    p2E2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E2, 2, 5, Main.shipList2))
    p2E3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E3, 3, 5, Main.shipList2))
    p2E4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E4, 4, 5, Main.shipList2))
    p2E5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E5, 5, 5, Main.shipList2))
    p2E6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E6, 6, 5, Main.shipList2))
    p2E7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E7, 7, 5, Main.shipList2))
    p2E8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E8, 8, 5, Main.shipList2))
    p2E9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E9, 9, 5, Main.shipList2))
    p2E10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2E10, 10, 5, Main.shipList2))
    p2colE = [p2E1, p2E2, p2E3, p2E4, p2E5, p2E6, p2E7, p2E8, p2E9, p2E10]

    p2F1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F1, 1, 6, Main.shipList2))
    p2F2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F2, 2, 6, Main.shipList2))
    p2F3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F3, 3, 6, Main.shipList2))
    p2F4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F4, 4, 6, Main.shipList2))
    p2F5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F5, 5, 6, Main.shipList2))
    p2F6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F6, 6, 6, Main.shipList2))
    p2F7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F7, 7, 6, Main.shipList2))
    p2F8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F8, 8, 6, Main.shipList2))
    p2F9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F9, 9, 6, Main.shipList2))
    p2F10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2F10, 10, 6, Main.shipList2))
    p2colF = [p2F1, p2F2, p2F3, p2F4, p2F5, p2F6, p2F7, p2F8, p2F9, p2F10]

    p2G1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G1, 1, 7, Main.shipList2))
    p2G2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G2, 2, 7, Main.shipList2))
    p2G3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G3, 3, 7, Main.shipList2))
    p2G4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G4, 4, 7, Main.shipList2))
    p2G5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G5, 5, 7, Main.shipList2))
    p2G6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G6, 6, 7, Main.shipList2))
    p2G7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G7, 7, 7, Main.shipList2))
    p2G8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G8, 8, 7, Main.shipList2))
    p2G9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G9, 9, 7, Main.shipList2))
    p2G10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2G10, 10, 7, Main.shipList2))
    p2colG = [p2G1, p2G2, p2G3, p2G4, p2G5, p2G6, p2G7, p2G8, p2G9, p2G10]

    p2H1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H1, 1, 8, Main.shipList2))
    p2H2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H2, 2, 8, Main.shipList2))
    p2H3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H3, 3, 8, Main.shipList2))
    p2H4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H4, 4, 8, Main.shipList2))
    p2H5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H5, 5, 8, Main.shipList2))
    p2H6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H6, 6, 8, Main.shipList2))
    p2H7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H7, 7, 8, Main.shipList2))
    p2H8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H8, 8, 8, Main.shipList2))
    p2H9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H9, 9, 8, Main.shipList2))
    p2H10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2H10, 10, 8, Main.shipList2))
    p2colH = [p2H1, p2H2, p2H3, p2H4, p2H5, p2H6, p2H7, p2H8, p2H9, p2H10]

    p2I1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I1, 1, 9, Main.shipList2))
    p2I2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I2, 2, 9, Main.shipList2))
    p2I3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I3, 3, 9, Main.shipList2))
    p2I4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I4, 4, 9, Main.shipList2))
    p2I5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I5, 5, 9, Main.shipList2))
    p2I6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I6, 6, 9, Main.shipList2))
    p2I7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I7, 7, 9, Main.shipList2))
    p2I8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I8, 8, 9, Main.shipList2))
    p2I9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I9, 9, 9, Main.shipList2))
    p2I10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2I10, 10, 9, Main.shipList2))
    p2colI = [p2I1, p2I2, p2I3, p2I4, p2I5, p2I6, p2I7, p2I8, p2I9, p2I10]

    p2J1 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J1, 1, 10, Main.shipList2))
    p2J2 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J2, 2, 10, Main.shipList2))
    p2J3 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J3, 3, 10, Main.shipList2))
    p2J4 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J4, 4, 10, Main.shipList2))
    p2J5 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J5, 5, 10, Main.shipList2))
    p2J6 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J6, 6, 10, Main.shipList2))
    p2J7 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J7, 7, 10, Main.shipList2))
    p2J8 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J8, 8, 10, Main.shipList2))
    p2J9 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J9, 9, 10, Main.shipList2))
    p2J10 = Button(frameGrid1, width=2, bg='blue', command=lambda: fireAttack(p2J10, 10, 10, Main.shipList2))
    p2colJ = [p2J1, p2J2, p2J3, p2J4, p2J5, p2J6, p2J7, p2J8, p2J9, p2J10]

    # Set the board to use the correct amount of buttons
    if (boardSize == 8):
        p2colA = [p2A1, p2A2, p2A3, p2A4, p2A5, p2A6, p2A7, p2A8]
        p2colB = [p2B1, p2B2, p2B3, p2B4, p2B5, p2B6, p2B7, p2B8]
        p2colC = [p2C1, p2C2, p2C3, p2C4, p2C5, p2C6, p2C7, p2C8]
        p2colD = [p2D1, p2D2, p2D3, p2D4, p2D5, p2D6, p2D7, p2D8]
        p2colE = [p2E1, p2E2, p2E3, p2E4, p2E5, p2E6, p2E7, p2E8]
        p2colF = [p2F1, p2F2, p2F3, p2F4, p2F5, p2F6, p2F7, p2F8]
        p2colG = [p2G1, p2G2, p2G3, p2G4, p2G5, p2G6, p2G7, p2G8]
        p2colH = [p2H1, p2H2, p2H3, p2H4, p2H5, p2H6, p2H7, p2H8]
        p2colsList = [p2colA, p2colB, p2colC, p2colD, p2colE, p2colF, p2colG, p2colH]

    else:
        p2colsList = [p2colA, p2colB, p2colC, p2colD, p2colE, p2colF, p2colG, p2colH, p2colI, p2colJ]

    for p2cols in p2colsList:
        for button in p2cols:
            button.grid(row=p2colsList.index(p2cols) + 1, column=p2cols.index(button) + 12)


# Runs the main function which declares all the ships and the board etc (for now)
Main.main()
# Main function call inside the GUI class
mainFunc()
# First frame that is loaded
raiseFrame(frameMenu)
root.mainloop()
