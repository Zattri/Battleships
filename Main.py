import Boat, Gameboard, Attack, Game, TKgui

shipList1 = []
shipList2 = []
# Main program definition
def main():
    newBoard = Gameboard.Board(10, 10)
    ship1 = Boat.Ship(1, 3)
    ship2 = Boat.Ship(1, 3)
    ship3 = Boat.Ship(1, 3)
    ship4 = Boat.Ship(1, 3)


    # Board declared properly just used for testing - newBoard.printBoard()
    ship1.placeShip(4, 4, "N", shipList1)
    ship2.placeShip(1, 1, "S", shipList1)
    ship3.placeShip(3, 3, "E", shipList1)
    ship4.placeShip(5, 5, "W", shipList1)

    print(Attack.checkHit(shipList1, 2, 5))
    print(Attack.checkHit(shipList1, 3, 5))
    print(Attack.checkHit(shipList1, 4, 5))
    print(Attack.checkHit(shipList1, 5, 5))
    print(Attack.checkHit(shipList1, 6, 5))

    """
    print("Ship 1")
    ship1.printStats()
    print("Ship 2")
    ship2.printStats()
    """

# Runs main program
#main()

