from .gameBoards import print_hunt_board
from .gameBoards import print_prob_board
from .playerShipPlacement import boardCheckValidate, validateLocationInput


# Need to refactor - should be added as an attribute to a player class
def printProbBoard(offPlayer):
    """prints out the probably board for a human player

    Args:
        offPlayer (CLASS): The offensive player
    """
    offPlayer.updateCumlativeProb()
    print_prob_board(offPlayer.cumlativeProb)


def fullShotValidation(offPlayer):
    while True:
        shot = validateLocationInput('Please enter your shot location'
                                     ' Use a letter between A and J'
                                     ' and a number between 1 and 10.'
                                     ' Use the example as the format A:9: ')
        pshot = checkHuntBoardShot(offPlayer, shot)
        if pshot is False:
            print(f'{shot} has already been fired at, please select a new'
                  ' location')
            continue
        else:
            return shot


def checkHuntBoardShot(offPlayer, shot):
    """Checks the shot to see if this location has been shot at already

    Args:
        offPlayer (CLASS): Offensive Player
        shot (STR): The location of the computer shot in string format,
        example A:5

    Returns:
        BOOL: Returns False if the location has been shot at and True
        if the shot is a valid location
    """
    tempShot = offPlayer.huntBoard.get(shot)
    if tempShot != ' ':
        return False
    else:
        return True


def playerShot(offPlayer):
    """This will validate the location of the player shot at.  If the shot is
    valid the shot location will be returned.  If not valid a request for a
    valid location will be sent.

    Args:
        offPlayer (CLASS): Offensive Player Class

    Returns:
        STR: The location of the computer shot in string format,
        example A:5
    """
    print_hunt_board(offPlayer.huntBoard)
    probBoardResults = boardCheckValidate('Would you like to print the'
                                          'probability matrix? (Y/N)\n')
    if probBoardResults is True:
        printProbBoard(offPlayer)
    shot = fullShotValidation(offPlayer)
    return shot
