from random import randint
import Gameboard, Main, Attack


# Declaration of the computer class, with difficulty variable
class Computer:
    def __init__(self, diff):
        self.difficulty = diff

    # Randomly fires a shot at an area on the board
    def fireShot(self):
        if self.difficulty == 1:
            print("I'm going easy on ya kid")
            xPos = randint(1, Main.newBoard.getWidth())
            yPos = randint(1, Main.newBoard.getHeight())
            print("AI Move - X:", xPos, "Y:", yPos, " - ", Attack.checkHit(Main.shipList1, xPos, yPos))

        if self.difficulty == 2:
            print("Kids like you should just burn in hell")

