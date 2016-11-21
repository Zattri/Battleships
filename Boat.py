class Ship:
    def __init__(self, team, length):
        self.__size = length
        self.__team = team
        self.__alive = True
        self.__xPos = None
        self.__yPos = None
        self.__orient = None

    # Sets a ship's location
    def placeShip(self, x, y, direction, shipList):
        self.__xPos = x
        self.__yPos = y
        self.__orient = direction
        shipList.append(self)

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

    # Get ship orientation
    def getOrient(self):
        return self.__orient

    # Mainly for testing
    def printStats(self):
        print("Length:",self.__size)
        print("Alive:",self.__alive)
        print("X:", self.__xPos, "Y:", self.__yPos)
        print("Team:",self.__team)
        print()


