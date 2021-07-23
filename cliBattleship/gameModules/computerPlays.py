import random


def computerShot(offPlayer):

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

    while True:
        pshot = random.choice(list(offPlayer.huntBoard.keys()))
        if offPlayer.huntBoard[pshot] != '0':
            pass
        else:
            return pshot


def randomComputerShotHuntMode(offPlayer):
    if offPlayer.huntMode is True:
        return(huntShotReturn(offPlayer))
    else:
        shot = randomComputerShot(offPlayer)
        return shot


def parityComputerShotHuntMode(offPlayer):
    if offPlayer.huntMode is True:
        return(huntShotReturn(offPlayer))
    else:
        shot = paritySearch(offPlayer)
        return shot


def ProbDensityComputerShotHuntMode(offPlayer):
    if offPlayer.huntMode is True:
        return(huntShotReturn(offPlayer))
    else:
        shot = probDensityComputerShot(offPlayer)
        return shot


def paritySearch(offPlayer):
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


def huntShotReturn(offPlayer):
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
    tempList = []
    for key, value in offPlayer.huntBoard.items():
        if val == value:
            tempList.append(key)
    return tempList
