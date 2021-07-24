import random
from .gameBoards import generateBoard


def northPlaceCheck(shipSize, yIndexStart, xStart, yAxis):
    """Given a start position on the y index and a ship size will check if
    if the y position is a valid location.

    Args:
        shipSize (INT): Ship size taken from Ship Class
        yIndexStart (INT): Start index location
        xStart (STR): The start position on the X Axis, is a letter
        yAxis (List): The y axis range in list

    Returns:
        [List]: If range is a valid location for the y axis start will return
        the valid list, else it will return false.
    """
    northShipPlace = []
    tempLastIndex = (yIndexStart + 1) - shipSize
    if tempLastIndex >= 0 and tempLastIndex <= 10:
        for i in range(tempLastIndex, yIndexStart + 1):
            northShipPlace.append(f'{yAxis[i]}:{xStart}')
        return northShipPlace
    else:
        return False


def southPlaceCheck(shipSize, yIndexStart, xStart, yAxis):
    """Given a start position on the y index and a ship size will check if
    if the y position is a valid location.

    Args:
        shipSize (INT): Ship size taken from Ship Class
        yIndexStart (INT): Start index location
        xStart (STR): The start position on the X Axis, is a letter
        yAxis (List): The y axis range in list

    Returns:
        [List]: If range is a valid location for the y axis start will return
        the valid list, else it will return false.
    """
    southShipPlace = []
    tempLastIndex = yIndexStart + shipSize
    if tempLastIndex >= 0 and tempLastIndex <= 10:
        for i in range(yIndexStart, tempLastIndex):
            southShipPlace.append(f'{yAxis[i]}:{xStart}')
        return southShipPlace
    else:
        return False


def westPlaceCheck(shipSize, xIndexStart, yStart, xAxis):
    """Given a start position on the x index and a ship size will check if
    if the x position is a valid location.

    Args:
        shipSize (INT): Ship size taken from Ship Class
        xIndexStart (INT): Start index location
        yStart (STR): The start position on the y Axis, is a letter
        xAxis ([INT]): The x axis range in a list

    Returns:
        [List]: If range is a valid location for the y axis start will return
        the valid list, else it will return false.
    """
    westShipPlace = []
    tempLastIndex = (xIndexStart + 1) - shipSize
    if tempLastIndex >= 0 and tempLastIndex <= 10:
        for i in range(tempLastIndex, xIndexStart + 1):
            westShipPlace.append(f'{yStart}:{xAxis[i]}')
        return westShipPlace

    else:
        return False


def eastPlaceCheck(shipSize, xIndexStart, yStart, xAxis):
    """Given a start position on the x index and a ship size will check if
    if the y position is a valid location.

    Args:
        shipSize (INT): Ship size taken from Ship Class
        xIndexStart (INT): Start index location
        yStart (STR): The start position on the Y Axis, is a letter
        yAxis ([INT]): The x x axis range in a list

    Returns:
        [List]: If range is a valid location for the y axis start will return
        the valid list, else it will return false.
    """
    eastShipPlace = []
    tempLastIndex = xIndexStart + shipSize
    if tempLastIndex >= 0 and tempLastIndex <= 10:
        for i in range(xIndexStart, tempLastIndex):
            eastShipPlace.append(f'{yStart}:{xAxis[i]}')
        return eastShipPlace
    else:
        return False


def placementOptions(loc1, ship, player):
    """Take a location, ship class, and player class calculates possible
    position ranges based upon start location of loc1

    Args:
        loc1 (STR): Start location in string form, example A:5
        ship (INT): Ship Size from the Ship Class
        player (Class): The Player object

    Returns:
        List: Contains a nest list of possible ship locations
        based upon start location
    """
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
    """Generates a random location of the game board

    Returns:
        STR: String in the format of <letter>:<number> example A:5
    """
    gameBoard = generateBoard()
    gameBoardList = [*gameBoard]
    possibleLocation = random.choice(gameBoardList)
    return possibleLocation


def findCarrierLocation(player):
    """Based on randomLocation() and possible carrier locations based on
    placementOptions() return a random list for the carrier to be placed in
    Args:
        player (Class): Player Class

    Returns:
        List: Location to place the player Carrier
    """
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
    """Based on randomLocation() and possible battleship locations based on
    placementOptions() return a random list for the carrier to be placed in
    Args:
        player (Class): Player Class

    Returns:
        List: Location to place the player Battleship
    """
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
    """Based on randomLocation() and possible cruiser locations based on
    placementOptions() return a random list for the carrier to be placed in
    Args:
        player (Class): Player Class

    Returns:
        List: Location to place the player Cruiser
    """
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
    """Based on randomLocation() and possible submarine locations based on
    placementOptions() return a random list for the carrier to be placed in
    Args:
        player (Class): Player Class

    Returns:
        List: Location to place the player Submarine
    """
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
    """Based on randomLocation() and possible destroyer locations based on
    placementOptions() return a random list for the carrier to be placed in
    Args:
        player (Class): Player Class

    Returns:
        List: Location to place the player Destroyer
    """
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
    """Automatically places all the ships

    Args:
        player (Class): The player class
    """
    player.placeCarrier(findCarrierLocation(player))
    player.placeBattleship(findBattleshipLocation(player))
    player.placeCruiser(findCruiserLocation(player))
    player.placeSubmarine(findSubmarineLocation(player))
    player.placeDestroyer(findDestroyerLocation(player))
