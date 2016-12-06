# Make instance of game
# Add ship list to instance
import Boat, Gameboard, Attack, Ai

# Needs a new name that isn
class theGame:
    def __init__(self):
        self.__shipList = [10]


def setShips(shipList1):
    global Main
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
    # Add other ships [WHEN DONE]
    # Create loops for each shipList (team)
    for ship in [ship1, ship2, ship3]:
        # Try catch the inputs
        xPos = input("X position: ")
        yPos = input("Y position: ")
        orient = input("Orrientation [N/E/S/W]: ")
        ship.placeShip(xPos, yPos, orient, shipList1)
