# Make instance of game
# Add ship list to instance
import Boat, Gameboard, Attack, Ai

def setShips(shipList1, shipList2):
    # Declare ships for Team 1
    ship1 = Boat.Ship(1, 1)
    ship2 = Boat.Ship(1, 2)
    ship3 = Boat.Ship(1, 3)
    ship4 = Boat.Ship(1, 4)
    ship5 = Boat.Ship(1, 5)

    # Declare ships for Team 2
    ship6 = Boat.Ship(1, 1)
    ship7 = Boat.Ship(1, 2)
    ship8 = Boat.Ship(1, 3)
    ship9 = Boat.Ship(1, 4)
    ship10 = Boat.Ship(1, 5)


    # Ship placement loop
    # Team 1 Ships
    print("Team 1 place your ships")
    for ship in [ship1, ship2]:
        while True:
            try:
                xPos = int(input("X position: "))
                break

            except ValueError:
                print("Entered value is not an integer within the board size")

        while True:
            try:
                yPos = int(input("Y position: "))
                break

            except ValueError:
                print("Entered value is not an integer within the board size")

        while True:
            orient = str(input("Orientation [N/E/S/W]: ")).lower()
            if orient != ("n" or "e" or "s" or "w"):
                print("Orientation must be either N, E, S or W")
            else:
                break
        ship.placeShip(xPos, yPos, orient, shipList1)

    # Team 2 Ships
    print("Team 2 place your ships")
    for ship in [ship6, ship7]:
        while True:
            try:
                xPos = int(input("X position: "))
                break

            except ValueError:
                print("Entered value is not an integer within the board size")

        while True:
            try:
                yPos = int(input("Y position: "))
                break

            except ValueError:
                print("Entered value is not an integer within the board size")

        while True:
            orient = str(input("Orientation [N/E/S/W]: ")).lower()
            if orient != ("n" or "e" or "s" or "w"):
                print("Orientation must be either N, E, S or W")
            else:
                break
        ship.placeShip(xPos, yPos, orient, shipList2)
