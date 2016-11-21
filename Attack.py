# Fires an attack at a specified position - Uses checkhit
def fireAttack(xPos, yPos):
    # Check position for ship
    # If the attack hits, redefine hit to 0 or 1 based off of hit condition
    print("Pew") # Change

# Check each ship in the enemy's ship list and returns if a ship is hit
def checkHit(shipList, xPos, yPos):
    hitStatus = False
    for i in range(len(shipList)):
        ship = shipList[i]
        # Check the orientation of the ship and if the hit is in the range of the length of the ship
        if ship.getOrient() == "N":
            if (ship.getLoc()[0] == xPos) and \
                    (yPos in range(ship.getLoc()[1] - ship.getSize() + 1, ship.getLoc()[1] + 1)):
                hitStatus = True

        elif ship.getOrient() == "E":
            if (xPos in range(ship.getLoc()[0], ship.getLoc()[0] + ship.getSize())) and \
                    (ship.getLoc()[1] == yPos):
                hitStatus = True

        elif ship.getOrient() == "S":
            if (ship.getLoc()[0] == xPos) and \
                    (yPos in range(ship.getLoc()[1], ship.getLoc()[1] + ship.getSize())):
                hitStatus = True

        elif ship.getOrient() == "W":
            if (xPos in range(ship.getLoc()[0] - ship.getSize() + 1, ship.getLoc()[0] + 1)) and \
                    (ship.getLoc()[1] == yPos):
                hitStatus = True

    return hitStatus

        # Down and Right + length
        # Up and Left - length



