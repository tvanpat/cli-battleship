from gameModules.players import Player
from gameModules.gameBoards import print_hunt_board
from gameModules.autoShipPlacement import placeAllships, placementOptions


def playerAutoPlacementValidate(prompt):
    while True:
        try:
            promptValue = int(input(prompt))
        except ValueError:
            print('Sorry, please enter either a 1 for computer '
                  'placement, and or 2 to place your own ships.')
            continue
        if promptValue == 1:
            return True
        elif promptValue == 2:
            return False
        else:
            print('Sorry, please enter either a 1 for computer '
                  'placement, or 2 to place your own ships.')
            continue


def validateLocationInput(prompt):
    xAxis = [i for i in range(1, 11)]
    yAxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    while True:
        promptValue = input(prompt)
        pos = promptValue.split(':')
        if len(pos) != 2:
            print('Either the location you provided is not in the '
                  'correct format or you are not using the correct range')
            continue
        try:
            xValue = int(pos[1])
        except ValueError:
            print('Either the location you provided is not in the '
                  'correct format or you are not using the correct range')
            continue

        if pos[0] not in yAxis:
            print('Either the location you provided is not in the '
                  'correct format or you are not using the correct range')
            continue
        elif xValue not in xAxis:
            print('Either the location you provided is not in the '
                  'correct format or you are not using the correct range')
            continue
        else:
            break
    return promptValue


def locationCollisionCheck(location, player):
    if location in player.masterPlacement:
        return True
    else:
        return False


def fullLocationInputValidation(player, playerShip):
    while True:
        tempLocation = validateLocationInput('Please enter the starting '
                                             'location for your '
                                             f'{playerShip.shipName}.  '
                                             'Use a letter between A and J '
                                             'and a number between 1 and 10. '
                                             'Use the example as the '
                                             'format A:9: ')
        locationCollisionCheckResults = locationCollisionCheck(tempLocation,
                                                               player)
        if locationCollisionCheckResults is True:
            print(f'{tempLocation} is currently in use, please select '
                  'another location')
            continue
        else:
            return tempLocation


def optionChoiceValidate(prompt, possEndLocs):
    while True:
        try:
            promptValue = int(input(prompt))
        except ValueError:
            print('Sorry, please enter one of the option numbers')
            continue
        options = [(x+1) for x in range(len(possEndLocs))]
        if promptValue in options:
            return possEndLocs[(promptValue-1)]
        else:
            print('Sorry, please enter one of the option numbers')
            continue


def chooseShipPlacement(player, locationOptions, shipType, validatedLocation):
    player.updateMasterBoard()
    tempBoard = player.masterBoard
    possEndLocs = []
    for i in range(len(locationOptions)):
        if locationOptions[i][0] == validatedLocation:
            possEndLocs.append(locationOptions[i][-1])
        else:
            possEndLocs.append(locationOptions[i][0])
        for j in locationOptions[i]:
            tempBoard[j] = str(i+1)
    tempBoard[validatedLocation] = shipType
    print_hunt_board(tempBoard)
    for i in range(len(possEndLocs)):
        print(f'Option {(i+ 1)} endpoint is {possEndLocs[i]}')
    endLocation = optionChoiceValidate('Type the option number for '
                                       'the endpoint placement: ', possEndLocs)
    return endLocation


def carrierOptions(player, playerShip):
    player.updateMasterBoard()
    while True:
        print_hunt_board(player.masterBoard)
        player.removeCarrier()
        validatedLocation = fullLocationInputValidation(player, playerShip)
        locationOptions = placementOptions(validatedLocation,
                                           player.carrier.size,
                                           player)
        if len(locationOptions) >= 1:
            break
        else:
            print('No valid ship locations found, please select a '
                  'new start position')
            continue
    endLocation = chooseShipPlacement(player,
                                      locationOptions,
                                      player.carrier.shipAbbr,
                                      validatedLocation)
    for i in locationOptions:
        if endLocation in i:
            player.placeCarrier(i)


def battleshipOptions(player, playerShip):
    player.updateMasterBoard()
    player.removeBattleship()
    while True:
        print_hunt_board(player.masterBoard)
        validatedLocation = fullLocationInputValidation(player, playerShip)
        locationOptions = placementOptions(validatedLocation,
                                           player.battleship.size,
                                           player)
        if len(locationOptions) >= 1:
            break
        else:
            print('No valid ship locations found, please select a '
                  'new start position')
            continue
    endLocation = chooseShipPlacement(player,
                                      locationOptions,
                                      player.battleship.shipAbbr,
                                      validatedLocation)
    for i in locationOptions:
        if endLocation in i:
            player.placeBattleship(i)


def cruiserOptions(player, playerShip):
    player.updateMasterBoard()
    player.removeCruiser()
    while True:
        print_hunt_board(player.masterBoard)
        validatedLocation = fullLocationInputValidation(player, playerShip)
        locationOptions = placementOptions(validatedLocation,
                                           player.cruiser.size,
                                           player)
        if len(locationOptions) >= 1:
            break
        else:
            print('No valid ship locations found, please select a '
                  'new start position')
            continue
    endLocation = chooseShipPlacement(player,
                                      locationOptions,
                                      player.cruiser.shipAbbr,
                                      validatedLocation)
    for i in locationOptions:
        if endLocation in i:
            player.placeCruiser(i)


def submarineOptions(player, playerShip):
    player.updateMasterBoard()
    player.removeSubmarine()
    while True:
        print_hunt_board(player.masterBoard)
        validatedLocation = fullLocationInputValidation(player, playerShip)
        locationOptions = placementOptions(validatedLocation,
                                           player.submarine.size,
                                           player)
        if len(locationOptions) >= 1:
            break
        else:
            print('No valid ship locations found, please select a '
                  'new start position')
            continue
    endLocation = chooseShipPlacement(player,
                                      locationOptions,
                                      player.submarine.shipAbbr,
                                      validatedLocation)
    for i in locationOptions:
        if endLocation in i:
            player.placeSubmarine(i)


def destroyerOptions(player, playerShip):
    player.updateMasterBoard()
    player.removeDestroyer()
    while True:
        print_hunt_board(player.masterBoard)
        validatedLocation = fullLocationInputValidation(player, playerShip)
        locationOptions = placementOptions(validatedLocation,
                                           player.destroyer.size,
                                           player)
        if len(locationOptions) >= 1:
            break
        else:
            print('No valid ship locations found, please select a '
                  'new start position')
            continue
    endLocation = chooseShipPlacement(player,
                                      locationOptions,
                                      player.destroyer.shipAbbr,
                                      validatedLocation)
    for i in locationOptions:
        if endLocation in i:
            player.placeDestroyer(i)


def playerAllPlacement(player):
    carrierOptions(player, player.carrier)
    battleshipOptions(player, player.battleship)
    cruiserOptions(player, player.cruiser)
    submarineOptions(player, player.submarine)
    destroyerOptions(player, player.destroyer)


def boardCheckValidate(prompt):
    while True:
        promptValue = input(prompt)
        if promptValue not in ['Y', 'N']:
            print('Please type Y or N')
            continue
        else:
            if promptValue == 'Y':
                return True
            else:
                return False


def shipChoiceValidate(player, prompt):
    while True:
        try:
            promptValue = int(input(prompt))
        except ValueError:
            print('Sorry your responce was not understood, please '
                  'enter 1, 2, 3, 4, 5, 6')
            continue
        if promptValue == 1:
            carrierOptions(player, player.carrier)
            return True
        elif promptValue == 2:
            battleshipOptions(player, player.battleship)
            return True
        elif promptValue == 3:
            cruiserOptions(player, player.cruiser)
            return True
        elif promptValue == 4:
            submarineOptions(player, player.submarine)
            return True
        elif promptValue == 5:
            destroyerOptions(player, player.destroyer)
            return True
        elif promptValue == 6:
            return False
        else:
            print('Sorry your responce was not understood, please '
                  'enter 1, 2, 3, 4, 5, 6')
            continue


def finalPlacementCheck(tempPlayer, player):
    while True:
        tempPlayer.updateMasterBoard()
        print_hunt_board(tempPlayer.masterBoard)
        boardResponce = boardCheckValidate('Would you like to make changes '
                                           'to your ship locations? Press Y '
                                           'for yes and N for No\n')
        if boardResponce is True:
            shipChoiceResult = shipChoiceValidate(tempPlayer, 'Which ship '
                                                  'would you like to replace '
                                                  '\nType 1 for Carrier'
                                                  '\nType 2 for Battleship'
                                                  '\nType 3 for Cruiser'
                                                  '\nType 4 for Submarine'
                                                  '\nType 5 for Destroyer'
                                                  '\nType 6 if you do not '
                                                  'want to make any changes'
                                                  '\n')
            if shipChoiceResult is True:
                continue
            else:
                break
        else:
            break
    player.placeCarrier(tempPlayer.carrier.placement)
    player.placeBattleship(tempPlayer.battleship.placement)
    player.placeCruiser(tempPlayer.cruiser.placement)
    player.placeSubmarine(tempPlayer.submarine.placement)
    player.placeDestroyer(tempPlayer.destroyer.placement)


def playerPlacement(player):
    autoShipPlacement = playerAutoPlacementValidate('Press 1 if you would like'
                                                    ' the computer to select '
                                                    'your ship locations.'
                                                    ' \nPress 2 if you want to'
                                                    ' place your own ships\n')
    # Create a tempPlayer object to store temp ship placements
    tempPlayer = Player()
    if autoShipPlacement is True:
        placeAllships(tempPlayer)
    else:
        playerAllPlacement(tempPlayer)
    finalPlacementCheck(tempPlayer, player)
