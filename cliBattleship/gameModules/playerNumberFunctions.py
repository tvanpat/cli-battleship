from .gameFunctions import randomPlayer, fullTurn
from .computerPlays import computerShot
from .playerPlays import playerShot


def printTurnResult(turnResult):
    """Prints the results of the turn, only used in 1 or 2 person games.

    Args:
        turnResult (DICT): Takes a dictionary of the turn result in json format
    """
    if turnResult.get('shotResult') == 'M':
        print(f'{turnResult.get("offPlayer")} fired at '
              f'{turnResult.get("shot")} and missed.')
    elif turnResult.get('shotResult') == 'H':
        if turnResult.get('shipSunk') is None:
            print(f'{turnResult.get("offPlayer")} fired at'
                  f'{turnResult.get("shot")} and hit '
                  f'{turnResult.get("defPlayer")}\'s ship.')
        else:
            print(f'{turnResult.get("offPlayer")} fired at '
                  f'{turnResult.get("shot")} and sunk '
                  f'{turnResult.get("defPlayer")}\'s '
                  f'{turnResult.get("shipSunk")}.')


def ComputerGameFunction(player1, player2):
    """This is a single game function for computer only play.  The player
    class for each player must be initialized before this can be called.
    Once called it will play the entire game and return a game log.

    Args:
        player1 (Class): The Player 1 class
        player2 (Class): The Player 2 class

    Returns:
        DICT: The full game log in a diction / json format
    """
    gameLog = []
    players = randomPlayer(player1, player2)
    offPlayer = players[0]
    defPlayer = players[1]
    gameInProgress = True
    while gameInProgress is True:
        shot = computerShot(offPlayer)
        offPlayer.lastShot = shot
        turnResult = fullTurn(shot, offPlayer, defPlayer)
        gamestatus = turnResult.get('gameStatus', 'in-progress')
        shotResult = turnResult.get('shotResult')
        offPlayer.lastShotResult = shotResult
        if gamestatus == 'over':
            gameLog.append(turnResult)
            gameInProgress = False
        else:
            shotResult = turnResult.get('shotResult', 'Error')
            offPlayer.huntBoard[shot] = shotResult
            gameLog.append(turnResult)
            tempOffPlayer = offPlayer
            offPlayer = defPlayer
            defPlayer = tempOffPlayer

    return gameLog


def OnePlayerGameFunction(player1, player2):
    """This is a single game function for 1 person play.  The player
    class for each player must be initialized before this can be called.
    Once called it will play the entire game and print out a turn results
    after each turn.

    Args:
        player1 (Class): The Player 1 class
        player2 (Class): The Player 2 class
    """
    gameLog = []
    players = randomPlayer(player1, player2)
    offPlayer = players[0]
    defPlayer = players[1]
    gameInProgress = True
    while gameInProgress is True:
        if offPlayer.computer is True:
            shot = computerShot(offPlayer)
        else:
            shot = playerShot(offPlayer)
        offPlayer.lastShot = shot
        turnResult = fullTurn(shot, offPlayer, defPlayer)
        gamestatus = turnResult.get('gameStatus', 'in-progress')
        shotResult = turnResult.get('shotResult')
        offPlayer.lastShotResult = shotResult
        if gamestatus == 'over':
            gameLog.append(turnResult)
            gameInProgress = False
        else:
            shotResult = turnResult.get('shotResult', 'Error')
            offPlayer.huntBoard[shot] = shotResult
            gameLog.append(turnResult)
            printTurnResult(turnResult)
            tempOffPlayer = offPlayer
            offPlayer = defPlayer
            defPlayer = tempOffPlayer
