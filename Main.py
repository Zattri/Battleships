import Boat, Gameboard
from Game import setShips
from fileFuncts import saveFile

# Ship list 1 is for player 2, and ship list 2 is for player 1, don't get confused =)
shipList1 = []
shipList2 = []
newBoard = Gameboard.Board(10, 10)

# Doesn't work currently
# compPlayer = Ai.Computer(1)
# gameInst = Game()
# Main program definition




def main():

    # Test ship setup
    # ===========================================
    ship1 = Boat.Ship(1, 3)
    ship2 = Boat.Ship(1, 4)
    ship3 = Boat.Ship(1, 3)
    ship4 = Boat.Ship(1, 4)

    ship1.placeShip(1, 1, "s", shipList1)
    ship2.placeShip(2, 2, "s", shipList1)
    ship3.placeShip(3, 3, "s", shipList2)
    ship4.placeShip(4, 4, "s", shipList2)
    # ===========================================

    # Save file test
    #fileFuncts.saveFile(shipList1, shipList2)

    # Ship lists are switched here to avoid confusion
    #setShips(shipList2, shipList1, newBoard)
