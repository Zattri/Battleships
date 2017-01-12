import Boat, Gameboard, Attack, Ai, fileFuncts, Game
from Game import setShips

shipList1 = []
shipList2 = []
newBoard = Gameboard.Board(10, 10)

# Doesn't work currently
# compPlayer = Ai.Computer(1)
# gameInst = Game()
# Main program definition




def main():

    # Save file test
    #fileFuncts.saveFile(shipList1, shipList2)

    setShips(shipList1, shipList2, newBoard)

# Runs main program
#main()
#setShips(shipList1, shipList2, newBoard)
