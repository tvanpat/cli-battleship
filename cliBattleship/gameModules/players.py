from .gameBoards import generateBoard, generateXaxis, generateYaxis


class Ship:
    """A Class to represent a ship
    """
    def __init__(self, size, shipAbbr, shipName):
        """
        Constructs all the necessary attributes for the class object.

        Parameters
        ----------
            operational : bool
                Is the ship operational
            size : int
                The Default size of the ship, number of hits the ship has
            hitsRemaining : int
                The number of hits remaining on the ship
            placement: list
                A list containing the locations of the ship.
            shipAbbr: str
                The ship abbreviation
            shipName: str
                The standard name for the ship
        """
        self.operational = True
        self.size = size
        self.hitsRemaining = size
        self.placement = []
        self.shipAbbr = shipAbbr
        self.shipName = shipName


class Player:
    """A Class to represent a player
    """
    def __init__(self, computer=False, computerLevel=0):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            nanem : str
                name of the person
            computer : bool
                bool representing if the player is a computer
            computerLevel : int
                level of the computer
            huntMode : bool
                reprenting if the player is in hunt mode
            huntModeStartShot : str
                the shot that put the player into hunt mode
            lastShotResult : str
                represents the result of the last shot H or M
            huntBoard : dict
                board representing the shot fired by the place
            shipCount : int
                number of ships the player currently has
            moveCount : int
                number of moves the player has made
            masterPlacement : list
                a list containing the locations of all player ships
            masterBoard : dict
                a dictionary containing the location and ship types
            carrier : Class
                initiates the carrier as a subclass of player
            battleship : Class
                initiates the battleship as a subclass of player
            cruiser : Class
                initiates the cruiser as a subclass of player
            submarine : Class
                initiates the submarine as a subclass of player
            destroyer : Class
                initiates the destroyer as a subclass of player
            xAxis : list
                a list of the x axis of the game
            yAxis : list
                a list of the y axis
        """
        self.name = None
        self.computer = computer
        self.computerLevel = computerLevel
        self.huntMode = False
        self.huntModeStartShot = 0
        self.lastShotResult = 'M'
        self.huntBoard = generateBoard()
        self.shipCount = 5
        self.moveCount = 0
        self.masterPlacement = []
        self.masterBoard = {}
        self.carrier = Ship(5, 'C', 'Carrier')
        self.battleship = Ship(4, 'B', 'Battleship')
        self.cruiser = Ship(3, 'c', 'Cruiser')
        self.submarine = Ship(3, 'S', 'Submarine')
        self.destroyer = Ship(2, 'D', 'Destroyer')
        self.xAxis = generateXaxis()
        self.yAxis = generateYaxis()
        self.carrierProb = 0
        self.battleshipProb = 0
        self.cruiserProb = 0
        self.submarineProb = 0
        self.destroyerProb = 0
        self.cumlativeProb = 0

    def reduceShipCount(self):
        self.shipCount -= 1

    def reduceCarrierCount(self):
        self.carrier.hitsRemaining -= 1

    def reduceBattleshipCount(self):
        self.battleship.hitsRemaining -= 1

    def reduceCruiserCount(self):
        self.cruiser.hitsRemaining -= 1

    def reduceSubmarineCount(self):
        self.submarine.hitsRemaining -= 1

    def reduceDestroyerCount(self):
        self.destroyer.hitsRemaining -= 1

    def setHuntMode(self, setting):
        self.huntMode = setting

    def placeCarrier(self, positionList):
        self.carrier.placement = positionList
        self.masterPlacement.extend(positionList)

    def placeBattleship(self, positionList):
        self.battleship.placement = positionList
        self.masterPlacement.extend(positionList)

    def placeCruiser(self, positionList):
        self.cruiser.placement = positionList
        self.masterPlacement.extend(positionList)

    def placeSubmarine(self, positionList):
        self.submarine.placement = positionList
        self.masterPlacement.extend(positionList)

    def placeDestroyer(self, positionList):
        self.destroyer.placement = positionList
        self.masterPlacement.extend(positionList)

    def removeCarrier(self):
        for i in self.carrier.placement:
            self.masterBoard[i] = '0'
            if i in self.masterPlacement:
                self.masterPlacement.remove(i)
            self.carrier.placement = []

    def removeBattleship(self):
        for i in self.battleship.placement:
            self.masterBoard[i] = '0'
            if i in self.masterPlacement:
                self.masterPlacement.remove(i)
            self.battleship.placement = []

    def removeCruiser(self):
        for i in self.cruiser.placement:
            self.masterBoard[i] = '0'
            if i in self.masterPlacement:
                self.masterPlacement.remove(i)
            self.cruiser.placement = []

    def removeSubmarine(self):
        for i in self.submarine.placement:
            self.masterBoard[i] = '0'
            if i in self.masterPlacement:
                self.masterPlacement.remove(i)
            self.submarine.placement = []

    def removeDestroyer(self):
        for i in self.destroyer.placement:
            self.masterBoard[i] = '0'
            if i in self.masterPlacement:
                self.masterPlacement.remove(i)
            self.destroyer.placement = []

    def checkShotMaster(self, shot):
        if shot in self.masterPlacement:
            return True
        else:
            return False

    def checkCarrierShot(self, shot):
        if shot in self.carrier.placement:
            return True
        else:
            return False

    def checkBattleshipShot(self, shot):
        if shot in self.battleship.placement:
            return True
        else:
            return False

    def checkCruiserShot(self, shot):
        if shot in self.cruiser.placement:
            return True
        else:
            return False

    def checkSubmarineShot(self, shot):
        if shot in self.submarine.placement:
            return True
        else:
            return False

    def checkDestroyerShot(self, shot):
        if shot in self.destroyer.placement:
            return True
        else:
            return False

    def checkForMiss(self, currentList):
        for i in currentList:
            if self.huntBoard[i] == 'M':
                return True
        return False

    def createHorizonalList(self):
        horizontalList = []
        for y in self.yAxis:
            newList = []
            for x in self.xAxis:
                pos = f'{y}:{x}'
                newList.append(pos)
            horizontalList.append(newList)
        return horizontalList

    def createVerticalList(self):
        verticalList = []
        for x in self.xAxis:
            newList = []
            for y in self.yAxis:
                pos = f'{y}:{x}'
                newList.append(pos)
            verticalList.append(newList)
        return verticalList

    def updateHorizontalProb(self, shipSize):
        horizontalCount = generateBoard()
        horizontalList = self.createHorizonalList()
        for i in horizontalList:
            newStart = 0
            newStop = shipSize
            for j in range(len(i)):
                if j + shipSize <= len(i):
                    tempList = (i[newStart:newStop])
                    newStart += 1
                    newStop += 1
                    if self.checkForMiss(tempList) is not True:
                        tempCount = 1
                    else:
                        tempCount = 0

                    for k in tempList:
                        tempX = int(horizontalCount[k])
                        tempX = tempX + tempCount
                        horizontalCount[k] = tempX

        return horizontalCount

    def updateVerticalProb(self, shipSize):
        verticalCount = generateBoard()
        verticalList = self.createVerticalList()
        for i in verticalList:
            newStart = 0
            newStop = shipSize
            for j in range(len(i)):
                if j + shipSize <= len(i):
                    tempList = (i[newStart:newStop])
                    newStart += 1
                    newStop += 1
                    if self.checkForMiss(tempList) is not True:
                        tempCount = 1
                    else:
                        tempCount = 0

                    for k in tempList:
                        tempX = int(verticalCount[k])
                        tempX = tempX + tempCount
                        verticalCount[k] = tempX

        return verticalCount

    def updateTotalProb(self, shipSize):
        totalProb = {}
        horizontalProb = self.updateHorizontalProb(shipSize)
        verticalProb = self.updateVerticalProb(shipSize)
        for y in self.yAxis:
            for x in self.xAxis:
                pos = f'{y}:{x}'
                xCount = horizontalProb[pos]
                yCount = verticalProb[pos]
                totalProb[pos] = (xCount + yCount)
        return totalProb

    def updateCumlativeProb(self):
        tempcumlativeProb = {}
        self.carrierProb = self.updateTotalProb(self.carrier.size)
        self.battleshipProb = self.updateTotalProb(self.battleship.size)
        self.cruiserProb = self.updateTotalProb(self.cruiser.size)
        self.submarineProb = self.updateTotalProb(self.submarine.size)
        self.destroyerProb = self.updateTotalProb(self.destroyer.size)
        for y in self.yAxis:
            for x in self.xAxis:
                pos = f'{y}:{x}'
                carrierCount = self.carrierProb[pos]
                battleshipCount = self.battleshipProb[pos]
                cruiserCount = self.cruiserProb[pos]
                submarineCount = self.submarineProb[pos]
                destroyerCount = self.destroyerProb[pos]
                tempCount = (carrierCount +
                             battleshipCount +
                             cruiserCount +
                             submarineCount +
                             destroyerCount)
                tempcumlativeProb[pos] = tempCount
        self.cumlativeProb = tempcumlativeProb

    def updateMasterBoard(self):
        self.masterBoard = generateBoard()
        for i in self.carrier.placement:
            self.masterBoard[i] = 'C'
        for i in self.battleship.placement:
            self.masterBoard[i] = 'B'
        for i in self.cruiser.placement:
            self.masterBoard[i] = 'c'
        for i in self.submarine.placement:
            self.masterBoard[i] = 'S'
        for i in self.destroyer.placement:
            self.masterBoard[i] = 'D'
