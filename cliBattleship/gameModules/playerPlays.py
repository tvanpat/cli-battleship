from .gameBoards import print_hunt_board
from .gameBoards import print_prob_board
from .playerShipPlacement import boardCheckValidate, validateLocationInput

def printProbBoard(offPlayer):
    offPlayer.updateCumlativeProb()
    print_prob_board(offPlayer.cumlativeProb)


def fullShotValidation(offPlayer):
    while True:
        shot = validateLocationInput('Please enter your shot location '
                              'Use a letter between A and J '
                              'and a number between 1 and 10. '
                              'Use the example as the format A:9: ')
        pshot = checkHuntBoardShot(offPlayer, shot)
        if pshot is False:
            print(f'{shot} has already been fired at, please select a new location')
            continue
        else:
            return shot


def checkHuntBoardShot(offPlayer, shot):
        if offPlayer.huntBoard[shot] != ' ':
            return False
        else:
            return True


def playerShot(offPlayer):
    print_hunt_board(offPlayer.huntBoard)
    probBoardResults = boardCheckValidate('Would you like to print the probability matrix? (Y/N)\n')
    if probBoardResults is True:
        printProbBoard(offPlayer)
    shot = fullShotValidation(offPlayer)     