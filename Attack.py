# Check each ship in the enemy's ship list and returns if a ship is hit
def checkHit(shipList, xPos, yPos):
    hitStatus = False
    for i in range(len(shipList)):
        ship = shipList[i]
        # Check the orientation of the ship and if the hit is in the range of the length of the ship
        if ship.getOrient().lower() == "n":
            if (ship.getLoc()[0] == xPos) and (yPos in range(ship.getLoc()[1] - ship.getSize() + 1, ship.getLoc()[1] + 1)):
                # Get the location of the hit on the ship
                hitLocation = yPos - (ship.getLoc()[1] + 1)
                # For testing
                #print("Hit:", hitLocation)
                ship.takeHit(hitLocation, shipList)
                # If hit is true, break check loop
                hitStatus = True
                break

        elif ship.getOrient().lower() == "e":
            if (xPos in range(ship.getLoc()[0], ship.getLoc()[0] + ship.getSize())) and \
                    (ship.getLoc()[1] == yPos):
                # Get the location of the hit on the ship
                hitLocation = (xPos - ship.getLoc()[0])
                # For testing
                #print("Hit:", hitLocation)
                ship.takeHit(hitLocation, shipList)
                # If hit is true, break check loop
                hitStatus = True
                break

        elif ship.getOrient().lower() == "s":
            if (ship.getLoc()[0] == xPos) and \
                    (yPos in range(ship.getLoc()[1], ship.getLoc()[1] + ship.getSize())):
                # Get the location of the hit on the ship
                hitLocation = (yPos - ship.getLoc()[1])
                # For testing
                #print("Hit:", hitLocation)
                ship.takeHit(hitLocation, shipList)
                # If hit is true, break check loop
                hitStatus = True
                break

        elif ship.getOrient().lower() == "w":
            if (xPos in range(ship.getLoc()[0] - ship.getSize() + 1, ship.getLoc()[0] + 1)) and \
                    (ship.getLoc()[1] == yPos):
                # Get the location of the hit on the ship
                hitLocation = (xPos - ship.getLoc()[0] + 1)
                # For testing
                #print("Hit:", hitLocation)
                ship.takeHit(hitLocation, shipList)
                # If hit is true, break check loop
                hitStatus = True
                break

    return hitStatus

    # Down and Right + length
    # Up and Left - length



