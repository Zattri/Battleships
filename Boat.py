# List of ship types used for stating which ship has been sunk
shipType = ["Submarine", "Destroyer", "Cruiser", "Battleship", "Aircraft Carrier"]

class Ship:
    def __init__(self, team, length):
        self.__team = team
        self.__size = length
        self.__hits = []
        self.__alive = True
        self.__xPos = None
        self.__yPos = None
        self.__orient = None

    # Sets a ship's location
    def placeShip(self, x, y, direction, shipList):
        self.__xPos = x
        self.__yPos = y
        self.__orient = direction.lower()
        shipList.append(self)

    # Adds a hit to the list of hits taken to the ship
    def takeHit(self, location, shipList):
        if (location not in self.__hits):
            self.__hits.append(location)
            self.checkAlive(shipList)

    # Validates whether the ship is still alive after a hit, if not it declares that it was sunk and removes it from the list
    def checkAlive(self, shipList):
        if (len(self.__hits) == self.__size):
            self.__alive = False
            self.removeShip(shipList)

    # Removes a ship from the shipList once it is sunk
    def removeShip(self, shipList):
        if (self.__team == 1):
            print("Player 1 has lost", shipType[self.__size - 1])
        else:
            print("Player 2 has lost", shipType[self.__size - 1])
        shipTeam = self.getTeam()
        shipList.remove(self)
        # If after removal a shiplist contains no ships, there is a winner
        if (shipList == []):
            if (shipTeam == 1):
                print("Player 2 has won the match!")

            else:
                print("Player 1 has won the match!")


    # Gets the location of this ship
    def getLoc(self):
        return self.__xPos, self.__yPos

    # Gets the life status of this ship
    def getAlive(self):
        return self.__alive

    # Gets the team of the ship
    def getTeam(self):
        return self.__team

    # Get the size of the ship
    def getSize(self):
        return self.__size

    def getName(self):
        return shipType[self.__size - 1]

    # Get ship orientation
    def getOrient(self):
        return self.__orient

    # Mainly for testing
    def printStats(self):
        print("Length:",self.__size)
        print("Alive:",self.__alive)
        print("X:", self.__xPos, "Y:", self.__yPos, "Orient:", self.__orient)
        print("Team:",self.__team)
        print()

    # Used for sending strings back to the save function
    def stringStats(self):
        # Ships location
        locString = "Loc," + str(self.__xPos) + "," + str(self.__yPos) + "," + self.__orient
        # Length of the ship
        lenString = "Len," + str(self.__size)
        # The location of any hits the ship took
        hitString = "Hits,"
        for i in self.__hits:
            hitString += str(self.__hits[i])

        return locString, lenString, hitString
