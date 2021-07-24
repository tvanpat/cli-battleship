import random


def computerShot(offPlayer):
    """Based upon player computer setting calls the correct computer shot
    selection function.

    Args:
        offPlayer (Class): The Offensive Player

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    if offPlayer.computerLevel == 0:
        # Random shot
        shot = randomComputerShot(offPlayer)

    elif offPlayer.computerLevel == 1:
        shot = randomComputerShotHuntMode(offPlayer)

    elif offPlayer.computerLevel == 2:
        shot = parityComputerShotHuntMode(offPlayer)

    elif offPlayer.computerLevel == 3:
        offPlayer.updateCumlativeProb()
        shot = probDensityComputerShot(offPlayer)

    elif offPlayer.computerLevel == 4:
        offPlayer.updateCumlativeProb()
        shot = ProbDensityComputerShotHuntMode(offPlayer)
    return shot


def randomComputerShot(offPlayer):
    """Selects a random location to shoot at, if location has previously been
    selected this function will select another random location.

    Args:
        offPlayer (Class): The offensive player class

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    while True:
        pshot = random.choice(list(offPlayer.huntBoard.keys()))
        if offPlayer.huntBoard[pshot] != '0':
            pass
        else:
            return pshot


def randomComputerShotHuntMode(offPlayer):
    """Checks if the computer player is in Hunt mode (last shot was a hit
    or there has been a hit but no ship sunk yet).  If player is in hunt mode
    will call the huntShotReturn() function, if not will call the
    randomComputerShot function.

    Args:
        offPlayer (Class): The offensive player class

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    if offPlayer.huntMode is True:
        return(huntShotReturn(offPlayer))
    else:
        shot = randomComputerShot(offPlayer)
        return shot


def parityComputerShotHuntMode(offPlayer):
    """Checks if the computer player is in Hunt mode (last shot was a hit
    or there has been a hit but no ship sunk yet).  If player is in hunt mode
    will call the huntShotReturn() function, if not will call the
    paritySearch function.

    Args:
        offPlayer (Class): The offensive player class

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    if offPlayer.huntMode is True:
        return(huntShotReturn(offPlayer))
    else:
        shot = paritySearch(offPlayer)
        return shot


def ProbDensityComputerShotHuntMode(offPlayer):
    """Checks if the computer player is in Hunt mode (last shot was a hit
    or there has been a hit but no ship sunk yet).  If player is in hunt mode
    will call the huntShotReturn() function, if not will call the
    probDensityComputerShot function.

    Args:
        offPlayer (Class): The offensive player class

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    if offPlayer.huntMode is True:
        return(huntShotReturn(offPlayer))
    else:
        shot = probDensityComputerShot(offPlayer)
        return shot


def paritySearch(offPlayer):
    """The parity search uses the checkboard method to search for enemy ships
    if no remaing shot are in the parity search space, the function will
    select a random location that has not been shot at.

    Args:
        offPlayer (Class): Offensive Player

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    keyList = []
    xAxis = [i for i in range(1, 11)]
    yAxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for y in range(len(yAxis)):
        for x in range(len(xAxis)):
            if (y % 2) == 0:
                if (x % 2) != 0:
                    tempShot = (f'{yAxis[y]}:{xAxis[x]}')
                    if offPlayer.huntBoard[tempShot] == '0':
                        keyList.append(tempShot)
            elif (y % 2) != 0:
                if (x % 2) == 0:
                    tempShot = (f'{yAxis[y]}:{xAxis[x]}')
                    if offPlayer.huntBoard[tempShot] == '0':
                        keyList.append(tempShot)
    if len(keyList) >= 1:
        return random.choice(keyList)
    else:
        tempList = getOffPlayerHuntboardkey('0', offPlayer)
        return random.choice(tempList)


def probDensityComputerShot(offPlayer):
    """Calls the player cumlativeProbabiltiy method to calculate current
    possibilities, will choose the highest probability.  The highest
    probability will be checked to ensure the shot is not a previous hit.  If
    shot is not a previous hit, function will return the shot, if a previous
    hit function will choose the next highest possibility


    Args:
        offPlayer (Class): Offensive Player

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    while True:
        tempSort = sorted(offPlayer.cumlativeProb.items(),
                          key=lambda x: x[1], reverse=True)
        while True:
            for i in tempSort:
                shotValue = offPlayer.huntBoard.get(i[0], " ")
                if shotValue != '0':
                    pass
                else:
                    return i[0]


# Need to refactor this function to make it cleaner
def huntShotReturn(offPlayer):
    """When Offensive Player is in Hunt Mode, this function create a list for
    the north possible locations, east, south, and west.  To narrow the search
    area for the next shot.  After all directional lists are returned the
    function will go to the north list if the next available location is a M
    the function will move to the east list and follow the same pattern.  If
    the north list contains a blank or H, the function will fire at that shot.

    Args:
        offPlayer (Class): The Offensive Player

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    xAxis = [i for i in range(1, 11)]
    yAxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    pos = offPlayer.huntModeStartShot.split(':')
    yShot = pos[0]
    xShot = int(pos[1])
    HuntDict = ['yAxisNorthHunt',
                'xAxisEastHunt',
                'yAxisSouthHunt',
                'xAxisWestHunt']
    for i in HuntDict:
        if i == 'yAxisNorthHunt':
            yShotIndex = (yAxis.index(yShot) - 1)
            if yShotIndex >= 0:
                possShot = (f'{yAxis[yShotIndex]}:{xShot}')
                if offPlayer.huntBoard[possShot] == 'M':
                    pass
                elif offPlayer.huntBoard[possShot] == 'H':
                    checkShotCycle = True
                    tempShotIndex = yShotIndex
                    while checkShotCycle is True:
                        tempShotIndex -= 1
                        if tempShotIndex >= 0:
                            nextPossShot = (f'{yAxis[tempShotIndex]}:{xShot}')
                            if offPlayer.huntBoard[nextPossShot] == 'M':
                                checkShotCycle = False
                            elif offPlayer.huntBoard[nextPossShot] == 'H':
                                continue
                            else:
                                return nextPossShot
                        else:
                            checkShotCycle = False
                else:
                    return possShot

        elif i == 'xAxisEastHunt':
            xShotIndex = (xAxis.index(xShot) + 1)
            if xShotIndex <= 9:
                possShot = (f'{yShot}:{xAxis[xShotIndex]}')
                if offPlayer.huntBoard[possShot] == 'M':
                    pass

                elif offPlayer.huntBoard[possShot] == 'H':
                    checkShotCycle = True
                    tempShotIndex = xShotIndex
                    while checkShotCycle is True:
                        tempShotIndex += 1
                        if tempShotIndex <= 9:
                            nextPossShot = (f'{yShot}:{xAxis[tempShotIndex]}')
                            if offPlayer.huntBoard[nextPossShot] == 'M':
                                checkShotCycle = False
                            elif offPlayer.huntBoard[nextPossShot] == 'H':
                                continue
                            else:
                                return nextPossShot
                        else:
                            checkShotCycle = False
                else:
                    return possShot

        elif i == 'yAxisSouthHunt':
            yShotIndex = (yAxis.index(yShot) + 1)
            if yShotIndex <= 9:
                possShot = (f'{yAxis[yShotIndex]}:{xShot}')
                if offPlayer.huntBoard[possShot] == 'M':
                    pass
                elif offPlayer.huntBoard[possShot] == 'H':
                    checkShotCycle = True
                    tempShotIndex = yShotIndex
                    while checkShotCycle is True:
                        tempShotIndex += 1
                        if tempShotIndex <= 9:
                            nextPossShot = (f'{yAxis[tempShotIndex]}:{xShot}')
                            if offPlayer.huntBoard[nextPossShot] == 'M':
                                checkShotCycle = False
                            elif offPlayer.huntBoard[nextPossShot] == 'H':
                                continue
                            else:
                                return nextPossShot
                        else:
                            checkShotCycle = False
                else:
                    return possShot
        else:
            xShotIndex = (xAxis.index(xShot) - 1)
            if xShotIndex >= 0:
                possShot = (f'{yShot}:{xAxis[xShotIndex]}')
                if offPlayer.huntBoard[possShot] == 'M':
                    pass

                elif offPlayer.huntBoard[possShot] == 'H':
                    checkShotCycle = True
                    tempShotIndex = xShotIndex
                    while checkShotCycle is True:
                        tempShotIndex -= 1
                        if tempShotIndex >= 0:
                            nextPossShot = (f'{yShot}:{xAxis[tempShotIndex]}')
                            if offPlayer.huntBoard[nextPossShot] == 'M':
                                checkShotCycle = False
                            elif offPlayer.huntBoard[nextPossShot] == 'H':
                                continue
                            else:
                                return nextPossShot
                        else:
                            checkShotCycle = False
                else:
                    return possShot


def getOffPlayerHuntboardkey(val, offPlayer):
    """This function will cycle through the Player huntboard looking for the
    next unused location and return a list of unused locations

    Args:
        val (STR): The location of the computer shot in string
        format, example A:5
        offPlayer (Class): The offensive player

    Returns:
        STR: The location of the computer shot in string format, example A:5
    """
    tempList = []
    for key, value in offPlayer.huntBoard.items():
        if val == value:
            tempList.append(key)
    return tempList
