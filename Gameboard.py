class Board:
    # Define the board giving it a height and width
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__boardArray = [[None]*width for x in range(height)]

    # Fetches height of board
    def getHeight(self):
        return self.__height

    # Fetches height of board
    def getWidth(self):
        return self.__width
