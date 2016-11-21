from tkinter import *
#from tkinter import ttk
import Attack, Main


# [ERROR] shipList1 is not defined
def fireAttack(x, y):
    print("X:",x,"Y:",y)
    # global shipList1
    # Attack.checkHit(shipList1, x, y)

def switchFrame(key):
    newFrame = frameDict[key]
    newFrame.tkraise()



# Main Function
"""
frame = ttk.Frame(root, padding = 10)
frame.grid(column = 0, row = 0)
frame.master.title("Battleships")

frame2 = ttk.Frame(root, padding = 10)
frame2.grid(column = 0, row = 0)
frame2.master.title("Battleships Frame 2")
"""


def initFrame1():
    # Initialise frame and set place in Dictionary
    frame1.grid(row = 0, column = 0, sticky="news")
    frameDict["Main"] = frame1

    # Adds Column labels to the label list
    # Change to board sizes if needed
    for i in range(1, 11):
        labelList.append(Label(frame1, text = i))
        labelList[-1].grid(row = 0, column = i + 1)

    # [MAIN GRID LOOP]
    for row in range(1, 11):
        # Adds Row labels to the label list
        labelList.append(Label(frame1, text = row))
        labelList[-1].grid(row = row + 1, column = 0)

        # [SECONDARY GRID LOOP]
        # Adds buttons for each row top left to bottom right
        for col in range(1, 11):
            loc = str(row) + "," + str(col)
            coordList.append(loc)
            buttonDict[coordList[-1]] = Button(frame1, width = 2)
            buttonDict[coordList[-1]]["command"] = lambda x = col, y = row: fireAttack(x, y)
            buttonDict[coordList[-1]].grid(row = row + 1, column = col + 1)

    Button(frame2, text="Switch frame", command = lambda:switchFrame("Second").grid(row = 0, column = 0)).grid(row =
                                                                                                               13, column = 2)

def initFrame2():
    frame2.grid(row = 0, column = 0, sticky="news")
    frameDict["Second"] = frame2

    Button(frame2, text="Hello world", command = print("Hello World")).grid(row = 1, column = 2)
    Button(frame2, text="Switch frame", command = lambda:switchFrame("Main").grid(row = 0, column = 0)).grid(row = 1,
                                                                                                             column = 1)

root = Tk()
labelList = []
coordList = []
buttonDict = {}
frameDict = {}
frame1 = Frame(root)
frame2 = Frame(root)

initFrame1()
initFrame2()
switchFrame("Main")
root.mainLoop()