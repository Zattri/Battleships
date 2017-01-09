from tkinter import *
from tkinter import ttk
import Attack, Main, Ai

# Global declarations
labelList = []
coordList = []
buttonDict = {}
boardSize = 10

# Root declaration
root = Tk()

# Frame declarations
framePlace = Frame(root)
frameGrid1 = Frame(root)
frameGrid2 = Frame(root)
frameMenu = Frame(root)

# [==================================================================================================================]

def fireAttack(button, x, y, shipList):
    # Prints the location of the attack and whether it hit or not - For testing
    #print("X:",x,"Y:",y, " - ", Attack.checkHit(shipList, x, y))
    if (Attack.checkHit(shipList, x, y) == True):
        changeColour(button, "red")
    else:
        changeColour(button, "grey")

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
    initBattleGrid1()

# Create the menu frame
def initMenu():
    Button(frameMenu, text="Attack Grid", command=lambda:raiseFrame(frameGrid1)).pack()
    Button(frameMenu, text="Ship Placement", command=lambda:raiseFrame(framePlace)).pack()
    Button(frameMenu, text="Size 8", command=lambda:changeBoardSize(8)).pack()
    Button(frameMenu, text="Size 10", command=lambda:changeBoardSize(10)).pack()


# Defines main running function for GUI
def mainFunc():
    # Set the frames to the base grid, give padding and a title to each frame
    for frame in (frameGrid1, frameGrid2, frameMenu, framePlace):
        frame.grid(row=0, column=0, sticky='news', padx = 10, pady = 10)
        frame.master.title("Battleships")


    # Initialise all the frames
    initBattleGrid1()
    initMenu()


# Define the main battlegrid frame
def initBattleGrid1():
    # Adds menu buttons and an AI fire button
    Button(frameGrid1, text="Menu", command=lambda: raiseFrame(frameMenu)).grid(row=13, column=2)
    Button(frameGrid1, text="AI", command=lambda: Main.compPlayer.fireShot()).grid(row=13, column=4)

    # Adds Column labels to the label list
    for col in range(1, boardSize+1):
        labelList.append(ttk.Label(frameGrid1, text=col))
        labelList[-1].grid(row=0, column=col)

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



# Runs the main function which declares all the ships and the board etc (for now)
Main.main()
# Main function call inside the GUI class
mainFunc()
# First frame that is loaded
raiseFrame(frameMenu)
root.mainloop()
