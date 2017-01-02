# Make instance of game
# Add ship list to instance
import Boat, Gameboard, Attack, Ai

def setShips(shipList1, shipList2, board):
    # Declare ships for Team 1
    ship1 = Boat.Ship(1, 1)
    ship2 = Boat.Ship(1, 2)
    ship3 = Boat.Ship(1, 3)
    ship4 = Boat.Ship(1, 4)
    ship5 = Boat.Ship(1, 5)

    # Declare ships for Team 2
    ship6 = Boat.Ship(2, 1)
    ship7 = Boat.Ship(2, 2)
    ship8 = Boat.Ship(2, 3)
    ship9 = Boat.Ship(2, 4)
    ship10 = Boat.Ship(2, 5)


    # Team 1 Ships input
    print("Team 1 place your ships")
    for ship in [ship1, ship2]:
        shipInputLoop(shipList1, ship, board)

    # Team 2 Ships input
    #print("Team 2 place your ships")
    #for ship in [ship6, ship7]:
    #    shipInputLoop(shipList2, ship, board)


# Input loop for entering ships onto the grid
def shipInputLoop(shipList, ship, board):
    # Outer loop - break after successfully placing a ship
    while True:
        # Inner loops for each input check - break after valid input
        while True:
            try:
                xPos = int(input("X position: "))
                if ((xPos < 0) or (xPos > board.getWidth())):
                    print("Position is not on the board")
                else:
                    break


            except ValueError:
                print("Entered value is not an integer within the board size")

        while True:
            try:
                yPos = int(input("Y position: "))
                if ((yPos < 0) or (yPos > board.getHeight())):
                    print("Position is not on the board")
                else:
                    break

            except ValueError:
                print("Entered value is not an integer within the board size")

        while True:
            orient = str(input("Orientation [N/E/S/W]: ")).lower()
            if (orient != (("n" or "e") or ("s" or "w"))):
                print("Orientation must be either N, E, S or W")
            else:
                break

        # Check spaces around selected ship location
        shipSize = ship.getSize()
        if (checkSpace(shipList, board, xPos, yPos, orient, shipSize) == True):
            ship.placeShip(xPos, yPos, orient, shipList)
            ship.printStats()
            break


# Checks the spaces around a location for ships, or if the ship will go off the edge
def checkSpace(shipList, board, x, y, orient, size):
    canPlace = True

    if (orient == "n"):
        for i in range(y, (y - size)):
            if (Attack.checkHit(shipList, x, i) == True):
                print("Ship cannot be placed here, it touches another ship")
                canPlace = False

    elif (orient == "e"):
        for i in range(x, (x + size)):
            if (Attack.checkHit(shipList, i, y) == True):
                print("Ship cannot be placed here, it touches another ship")
                canPlace = False

    elif (orient == "s"):
        for i in range(y, (y + size)):
            if (Attack.checkHit(shipList, x, i) == True):
                print("Ship cannot be placed here, it touches another ship")
                canPlace = False

    elif (orient == "w"):
        print("I am running")
        for i in range(x, (x - size)):
            if (Attack.checkHit(shipList, i, y) == True):
                print("Ship cannot be placed here, it touches another ship")
                canPlace = False

    print(canPlace)
    return canPlace
