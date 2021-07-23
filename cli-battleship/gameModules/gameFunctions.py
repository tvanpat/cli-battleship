import random


def fullTurn(shot, offPlayer, defPlayer):
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
    return getattr(getattr(defPlayer, ship.lower()), 'hitsRemaining')


def randomPlayer(player1, player2):
    offPlayer = random.choice([player1, player2])
    if offPlayer == player1:
        defPlayer = player2
    else:
        defPlayer = player1
    return(offPlayer, defPlayer)
