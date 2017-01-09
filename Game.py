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
    for ship in [ship1, ship2, ship3, ship4]:
        shipInputLoop(shipList1, ship, board)

    # Team 2 Ships input
    #print("Team 2 place your ships")
    #for ship in [ship6, ship7]:
    #    shipInputLoop(shipList2, ship, board)


# Input loop for entering ships onto the grid
def shipInputLoop(shipList, ship, board):
    print("Now placing - " + str(ship.getName()) + " [" + str(ship.getSize()) + "]")
    # Outer loop - break after successfully placing a ship
    while True:
        # Inner loops for each input check - break after valid input
        while True:
            orient = str(input("Orientation [N/E/S/W]: ")).lower()
            if (orient not in ["n", "s", "e", "w"]):
                print("Orientation must be either N, E, S or W")
            else:
                break

        if orient == "n":
            while True:
                try:
                    xPos = int(input("X position: "))
                    if ((xPos <= 0) or (xPos > board.getWidth())):
                        print("The ship is not fully positioned on the board")
                    else:
                        break

                except ValueError:
                    print("Entered value is not an integer within the board size")

            while True:
                try:
                    yPos = int(input("Y position: "))
                    if ((yPos - ship.getSize() < 0) or (yPos > board.getHeight())):
                        print("Position is not on the board")
                    else:
                        break

                except ValueError:
                    print("Entered value is not an integer within the board size")


        elif orient == "e":
            while True:
                try:
                    xPos = int(input("X position: "))
                    if ((xPos <= 0) or (xPos + ship.getSize() > board.getWidth() + 1)):
                        print("The ship is not fully positioned on the board")
                    else:
                        break

                except ValueError:
                    print("Entered value is not an integer within the board size")

            while True:
                try:
                    yPos = int(input("Y position: "))
                    if ((yPos <= 0) or (yPos > board.getHeight())):
                        print("Position is not on the board")
                    else:
                        break

                except ValueError:
                    print("Entered value is not an integer within the board size")


        elif orient == "s":
            while True:
                try:
                    xPos = int(input("X position: "))
                    if ((xPos <= 0) or (xPos > board.getWidth())):
                        print("The ship is not fully positioned on the board")
                    else:
                        break

                except ValueError:
                    print("Entered value is not an integer within the board size")

            while True:
                try:
                    yPos = int(input("Y position: "))
                    if ((yPos <= 0) or (yPos + ship.getSize() > board.getHeight() + 1)):
                        print("Position is not on the board")
                    else:
                        break

                except ValueError:
                    print("Entered value is not an integer within the board size")


        elif orient == "w":
            while True:
                try:
                    xPos = int(input("X position: "))
                    if ((xPos - ship.getSize() < 0) or (xPos > board.getWidth())):
                        print("The ship is not fully positioned on the board")
                    else:
                        break

                except ValueError:
                    print("Entered value is not an integer within the board size")

            while True:
                try:
                    yPos = int(input("Y position: "))
                    if ((yPos <= 0) or (yPos > board.getHeight())):
                        print("Position is not on the board")
                    else:
                        break

                except ValueError:
                    print("Entered value is not an integer within the board size")

        # Check spaces around selected ship location
        shipSize = ship.getSize()
        if (checkSpace(shipList, board, xPos, yPos, orient, shipSize) == True):
            ship.placeShip(xPos, yPos, orient, shipList)
            # For testing
            #ship.printStats()
            break

        else:
            print("There is already a ship positioned in that location")


# Checks the spaces around a location for ships, or if the ship will go off the edge
def checkSpace(shipList, board, x, y, orient, size):
    canPlace = True

    if (orient == "n"):
        for i in range(y, (y - size)):
            if (checkColision(shipList, x, i) == True):
                canPlace = False

    elif (orient == "e"):
        for i in range(x, (x + size)):
            if (checkColision(shipList, i, y) == True):
                canPlace = False

    elif (orient == "s"):
        for i in range(y, (y + size)):
            if (checkColision(shipList, x, i) == True):
                canPlace = False

    elif (orient == "w"):
        for i in range(x, (x - size)):
            if (checkColision(shipList, i, y) == True):
                canPlace = False

    # For testing
    # print("Placement -", canPlace)
    return canPlace

# Checks whether a ship will colide with another when placed
def checkColision(shipList, xPos, yPos):
    hitStatus = False
    for i in range(len(shipList)):
        ship = shipList[i]
        # Check the orientation of the ship and if the hit is in the range of the length of the ship
        if ship.getOrient().lower() == "n":
            if (ship.getLoc()[0] == xPos) and (
                yPos in range(ship.getLoc()[1] - ship.getSize() + 1, ship.getLoc()[1] + 1)):
                hitStatus = True
                break

        elif ship.getOrient().lower() == "e":
            if (xPos in range(ship.getLoc()[0], ship.getLoc()[0] + ship.getSize())) and \
                    (ship.getLoc()[1] == yPos):
                hitStatus = True
                break

        elif ship.getOrient().lower() == "s":
            if (ship.getLoc()[0] == xPos) and \
                    (yPos in range(ship.getLoc()[1], ship.getLoc()[1] + ship.getSize())):
                hitStatus = True
                break

        elif ship.getOrient().lower() == "w":
            if (xPos in range(ship.getLoc()[0] - ship.getSize() + 1, ship.getLoc()[0] + 1)) and \
                    (ship.getLoc()[1] == yPos):
                hitStatus = True
                break

    return hitStatus