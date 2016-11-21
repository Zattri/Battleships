class Board:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__boardArray = [[None]*width for x in range(height)]


    # Does printing - May not be needed
    def printBoard(self):
        for x in range(self.__height):
            for y in range(self.__width):
                print(self.__boardArray[x][y], sep = " ")
            print()

    # Fetches height of board
    def getHeight(self):
        return self.__height

    # Fetches height of board
    def getWidth(self):
        return self.__width