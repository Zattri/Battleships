
from tkinter import *

class firstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        """
        self.label = Label(master, text="My first GUI")
        self.label.pack()

        self.greetButton = Button(master, text="Greetings", command=self.greet)
        self.greetButton.pack(side=LEFT)

        self.quitButton = Button(master, text="Quit", command=master.quit)
        self.quitButton.grid(row=2, columnspan=2, sticky=W+E)


        self.okButton = Button(master, text="OK", command=self.ok)
        self.okButton.grid(row=1, column=1, sticky=W)

        self.okButton2 = Button(master, text="OK", command=self.ok)
        self.okButton2.grid(row=1, column=0, sticky=E)
        """

        self.north = Button(master, text="N")
        self.east = Button(master, text="E")
        self.south = Button(master, text="S")
        self.west = Button(master, text="W")

        self.north.grid(column = 1)
        self.east.grid(column = 2, row=1)
        self.west.grid(column = 0, row=1)
        self.south.grid(column = 1, row=2)


    def greet(self):
        print("Greetings")

    def ok(self):
        print("You pressed ok")

root = Tk()
myGui = firstGUI(root)
root.mainloop()