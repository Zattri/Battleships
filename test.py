from tkinter import *
from tkinter import ttk

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
frameGrid = Frame(root)
frameMenu = Frame(root)

# [==================================================================================================================]

# [ERROR] shipList1 is not defined
def fireAttack(x, y):
    print("X:",x,"Y:",y)
    # global shipList1
    # Attack.checkHit(shipList1, x, y)


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


def initFMenu():
    Button(frameMenu, text="Grid", command=lambda:raiseFrame(frameGrid)).pack()


def mainFunc():
    # Set the frames to the base grid, give padding and a title to each frame
    for frame in (f1, f2, f3, f4, frameGrid, frameMenu):
        frame.grid(row=0, column=0, sticky='news', padx = 10, pady = 10)
        frame.master.title("Battleships")


    # Initialise all the frames
    initFGrid()
    initFMenu()

    """
    #Template for making buttons and labels and attaching them to forms
    Button(f1, text='Go to Grid Frame', command=lambda:raise_frame(frameGrid)).pack()
    Label(f1, text='Grid Frame').pack()
    """

    # First frame that is loaded
    raiseFrame(frameMenu)
    root.mainloop()


# Main function call
mainFunc()