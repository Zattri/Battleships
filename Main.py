import Boat, Gameboard, Attack, Game, Ai

shipList1 = []
shipList2 = []
newBoard = Gameboard.Board(10, 10)

# Doesn't work currenlty
# compPlayer = Ai.Computer(1)

# Main program definition

def main():
    global Game
    Game.setShips(shipList1)
    # Board declared properly just used for testing - newBoard.printBoard()
    """
    print("Ship 1")
    ship1.printStats()
    print("Ship 2")
    ship2.printStats()
    """

# Runs main program
main()
