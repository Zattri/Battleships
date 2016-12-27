from tkinter import *
from tkinter import ttk

# Root declaration
root = Tk()

frame1 = Frame(root)
frame1.pack()

testButton = Button(frame1, text="Press Me", command = lambda: changeColour(testButton))
testButton.pack()

def changeColour(button):
    button["bg"] = "red"
    print(button)

frame1.tkraise()
root.mainloop()