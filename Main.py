import Gameboard
from Game import setShips


# Ship list 1 is for player 2, and ship list 2 is for player 1, don't get confused =)
shipList1 = []
shipList2 = []
newBoard = Gameboard.Board(8, 8)


def main():
    # Ship lists are switched here to avoid confusion
    setShips(shipList2, shipList1, newBoard)
