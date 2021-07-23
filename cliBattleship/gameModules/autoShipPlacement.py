import random
from .gameBoards import generateBoard


def northPlaceCheck(shipSize, yIndexStart, xStart, yAxis):
    northShipPlace = []
    tempLastIndex = (yIndexStart + 1) - shipSize
    if tempLastIndex >= 0 and tempLastIndex <= 10:
        for i in range(tempLastIndex, yIndexStart + 1):
            northShipPlace.append(f'{yAxis[i]}:{xStart}')
        return northShipPlace
    else:
        return False


def southPlaceCheck(shipSize, yIndexStart, xStart, yAxis):
    southShipPlace = []
    tempLastIndex = yIndexStart + shipSize
    if tempLastIndex >= 0 and tempLastIndex <= 10:
        for i in range(yIndexStart, tempLastIndex):
            southShipPlace.append(f'{yAxis[i]}:{xStart}')
        return southShipPlace
    else:
        return False


def westPlaceCheck(shipSize, xIndexStart, yStart, xAxis):
    westShipPlace = []
    tempLastIndex = (xIndexStart + 1) - shipSize
    if tempLastIndex >= 0 and tempLastIndex <= 10:
        for i in range(tempLastIndex, xIndexStart + 1):
            westShipPlace.append(f'{yStart}:{xAxis[i]}')
        return westShipPlace

    else:
        return False


def eastPlaceCheck(shipSize, xIndexStart, yStart, xAxis):
    eastShipPlace = []
    tempLastIndex = xIndexStart + shipSize
    if tempLastIndex >= 0 and tempLastIndex <= 10:
        for i in range(xIndexStart, tempLastIndex):
            eastShipPlace.append(f'{yStart}:{xAxis[i]}')
        return eastShipPlace
    else:
        return False


def placementOptions(loc1, ship, player):
    possLocList = []
    xAxis = [i for i in range(1, 11)]
    yAxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    pos = loc1.split(':')
    yStart = pos[0]
    xStart = int(pos[1])
    yIndexStart = (yAxis.index(yStart))
    xIndexStart = xAxis.index(xStart)
    northPlace = northPlaceCheck(ship, yIndexStart, xStart, yAxis)
    if northPlace is not False:
        if any(x in northPlace for x in player.masterPlacement):
            pass
        else:
            possLocList.append(northPlace)
    southPlace = southPlaceCheck(ship, yIndexStart, xStart, yAxis)
    if southPlace is not False:
        if any(x in southPlace for x in player.masterPlacement):
            pass
        else:
            possLocList.append(southPlace)
    westPlace = westPlaceCheck(ship, xIndexStart, yStart, xAxis)
    if westPlace is not False:
        if any(x in westPlace for x in player.masterPlacement):
            pass
        else:
            possLocList.append(westPlace)
    eastPlace = eastPlaceCheck(ship, xIndexStart, yStart, xAxis)
    if eastPlace is not False:
        if any(x in eastPlace for x in player.masterPlacement):
            pass
        else:
            possLocList.append(eastPlace)
    return possLocList


def randomLocation():
    gameBoard = generateBoard()
    gameBoardList = [*gameBoard]
    possibleLocation = random.choice(gameBoardList)
    return possibleLocation


def findCarrierLocation(player):
    while True:
        while True:
            possibleLocation = randomLocation()
            if possibleLocation in player.masterPlacement:
                continue
            else:
                break
        locationOptions = placementOptions(possibleLocation,
                                           player.carrier.size, player)
        if len(locationOptions) >= 1:
            return random.choice(locationOptions)
        else:
            continue


def findBattleshipLocation(player):
    while True:
        while True:
            possibleLocation = randomLocation()
            if possibleLocation in player.masterPlacement:
                continue
            else:
                break
        locationOptions = placementOptions(possibleLocation,
                                           player.battleship.size, player)
        if len(locationOptions) >= 1:
            return random.choice(locationOptions)
        else:
            continue


def findCruiserLocation(player):
    while True:
        while True:
            possibleLocation = randomLocation()
            if possibleLocation in player.masterPlacement:
                continue
            else:
                break
        locationOptions = placementOptions(possibleLocation,
                                           player.cruiser.size,
                                           player)
        if len(locationOptions) >= 1:
            return random.choice(locationOptions)
        else:
            continue


def findSubmarineLocation(player):
    while True:
        while True:
            possibleLocation = randomLocation()
            if possibleLocation in player.masterPlacement:
                continue
            else:
                break
        locationOptions = placementOptions(possibleLocation,
                                           player.submarine.size,
                                           player)
        if len(locationOptions) >= 1:
            return random.choice(locationOptions)
        else:
            continue


def findDestroyerLocation(player):
    while True:
        while True:
            possibleLocation = randomLocation()
            if possibleLocation in player.masterPlacement:
                continue
            else:
                break
        locationOptions = placementOptions(possibleLocation,
                                           player.destroyer.size,
                                           player)
        if len(locationOptions) >= 1:
            return random.choice(locationOptions)
        else:
            continue


def placeAllships(player):
    player.placeCarrier(findCarrierLocation(player))
    player.placeBattleship(findBattleshipLocation(player))
    player.placeCruiser(findCruiserLocation(player))
    player.placeSubmarine(findSubmarineLocation(player))
    player.placeDestroyer(findDestroyerLocation(player))
