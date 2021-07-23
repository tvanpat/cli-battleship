from gameModules.gameFunctions import randomPlayer, fullTurn
from gameModules.computerPlays import computerShot
from gameModules.playerPlays import playerShot


def printTurnResult(turnResult):
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
