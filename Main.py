import Boat, Gameboard, Attack, Ai
from Game import setShips

shipList1 = []
shipList2 = []
newBoard = Gameboard.Board(10, 10)

# Doesn't work currently
# compPlayer = Ai.Computer(1)
#gameInst = Game()
# Main program definition




def main():
    ship1 = Boat.Ship(1, 3)
    ship1.placeShip(1, 1, "s", shipList1)
    ship2 = Boat.Ship(1, 3)
    ship2.placeShip(5, 5, "e", shipList1)
    ship3 = Boat.Ship(1, 5)
    ship3.placeShip(4, 4, "s", shipList1)

    #setShips(shipList1, shipList2, newBoard)
    # Board declared properly just used for testing - newBoard.printBoard()
    """
    print("Ship 1")
    ship1.printStats()
    print("Ship 2")
    ship2.printStats()
    """

# Runs main program
main()
#setShips(shipList1, shipList2, newBoard)
