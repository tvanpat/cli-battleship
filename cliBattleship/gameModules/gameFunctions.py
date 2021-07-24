import random


# refactor to break into multiple simple functions
def fullTurn(shot, offPlayer, defPlayer):
    """This function represents a full turn of battleship. It takes an
    offensive player shot and checks the defense player placement board.
    If the shot is not in the placement board list it will return a json
    where the shot result is M.  If it is a hit it will place the offensive
    player into Hunt Mode and reduce the ship hit by one.  If the ship has zero
    hits remaining the function will reduce the defplayer ship count by one.
    If this results in no more ships the game will be over.

    Args:
        shot (STR): The location of the computer shot in string format,
        example A:5
        offPlayer (CLASS): The offensive player
        defPlayer (CLASS): The defense player

    Returns:
        DICT: returns a diction in json format of the shot results
    """
    offPlayer.moveCount += 1
    ship = checkShot(shot, defPlayer)
    if ship == 'Miss':
        return {'shot': shot,
                'shotResult': 'M',
                'gameStatus': 'in-progress',
                'offPlayer': offPlayer.name,
                'defPlayer': defPlayer.name,
                'offPlayerMoves': offPlayer.moveCount}
    else:
        reduceShipHits(ship, defPlayer)
        shipHitsTotal = checkShipHits(ship, defPlayer)
        if shipHitsTotal >= 1:
            if offPlayer.huntMode is False:
                offPlayer.huntMode = True
                offPlayer.huntModeStartShot = shot
            return {'shot': shot,
                    'shotResult': 'H',
                    'gameStatus': 'in-progress',
                    'offPlayer': offPlayer.name,
                    'defPlayer': defPlayer.name,
                    'offPlayerMoves': offPlayer.moveCount}
        else:
            defPlayer.shipCount -= 1
            offPlayer.huntMode = False
            if defPlayer.shipCount >= 1:
                return {'shot': shot, 'shotResult': 'H',
                        'shipSunk': ship,
                        'gameStatus': 'in-progress',
                        'offPlayer': offPlayer.name,
                        'defPlayer': defPlayer.name,
                        'offPlayerMoves': offPlayer.moveCount}
            else:
                return {'shot': shot,
                        'shotResult': 'H',
                        'gameStatus': 'over',
                        'gameWinner': offPlayer.name,
                        'offPlayer': offPlayer.name,
                        'defPlayer': defPlayer.name,
                        'offPlayerMoves': offPlayer.moveCount}


def checkShot(shot, defPlayer):
    """Checks the shot of the offensive player and returns the ship hit
    or Miss

    Args:
        shot (STR): The location of the computer shot in string format,
        defPlayer (CLASS): The defensive player

    Returns:
        STR: Returns the ship hit or Miss
    """
    if defPlayer.checkShotMaster(shot) is True:
        if defPlayer.checkCarrierShot(shot) is True:
            return "Carrier"
        elif defPlayer.checkBattleshipShot(shot) is True:
            return "Battleship"
        elif defPlayer.checkCruiserShot(shot) is True:
            return "Cruiser"
        elif defPlayer.checkSubmarineShot(shot) is True:
            return "Submarine"
        elif defPlayer.checkDestroyerShot(shot) is True:
            return "Destroyer"
    else:
        return 'Miss'


def reduceShipHits(ship, defPlayer):
    """Reduces the ship current count by one

    Args:
        ship (STR): String name of the ship that was hit
        defPlayer (CLASS): Defensive Player
    """
    if ship == 'Carrier':
        defPlayer.reduceCarrierCount()
    elif ship == 'Battleship':
        defPlayer.reduceBattleshipCount()
    elif ship == 'Cruiser':
        defPlayer.reduceCruiserCount()
    elif ship == 'Submarine':
        defPlayer.reduceSubmarineCount()
    elif ship == 'Destroyer':
        defPlayer.reduceDestroyerCount()


def checkShipHits(ship, defPlayer):
    """Checks the ship remaining hits of the defensive player

    Args:
        ship (STR): String name of the ship that was hit
        defPlayer (CLASS): Defensive Player

    Returns:
        INT: Remaining hits of defensive player ship
    """
    return getattr(getattr(defPlayer, ship.lower()), 'hitsRemaining')


def randomPlayer(player1, player2):
    """Chooses a random player to start the game

    Args:
        player1 (CLASS): Player 1
        player2 (CLASS): Player 2

    Returns:
        CLASS: assigns player the offensive or defensive.
    """
    offPlayer = random.choice([player1, player2])
    if offPlayer == player1:
        defPlayer = player2
    else:
        defPlayer = player1
    return(offPlayer, defPlayer)
