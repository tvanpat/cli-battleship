from gameModules.players import Player
from gameModules.autoShipPlacement import placeAllships
from gameModules.playerShipPlacement import playerPlacement
from gameModules.playerNumberFunctions import ComputerGameFunction
from gameModules.playerNumberFunctions import OnePlayerGameFunction


def playerCountCheck(prompt):
    while True:
        try:
            playerCount = int(input(prompt))

        except ValueError:
            print("Sorry, please enter either a 0, 1, or 2.")
            continue

        if playerCount not in [0, 1, 2]:
            print('Sorry, your responce must be 0, 1, or 2')
            continue

        else:
            break
    return playerCount


def computerLevelCheck(prompt):
    while True:
        try:
            compLevel = int(input(prompt))
        except ValueError:
            print("Sorry, please enter a number between 0 and 4.")
            continue
        if compLevel not in [0, 1, 2, 3, 4]:
            print('Sorry, your responce must be between 0 and 4')
            continue
        else:
            break
    return compLevel


def newComputerGame():
    player1 = Player()
    player1.computerLevel = computerLevelCheck('Please enter the level of '
                                               'computer player 1 (0 is the '
                                               'lowest 4 is the highest): ')
    player1.computer = True
    player2 = Player()
    player2.computerLevel = computerLevelCheck('Please enter the level of '
                                               'computer player 2 (0 is the '
                                               'lowest 4 is the highest): ')
    player2.computer = True
    placeAllships(player1)
    placeAllships(player2)
    player1.name = 'Player 1'
    player2.name = 'Player 2'
    gl = ComputerGameFunction(player1, player2)
    return gl[-1]


def newOnePlayerGame():
    player1 = Player()
    player1.name = input('Please enter the name of Player 1: ')
    player1.computer = False
    playerPlacement(player1)
    player2 = Player()
    player2.computerLevel = computerLevelCheck('Please enter the level of '
                                               'computer player 2 (1 is the '
                                               'lowest 4 is the highest) ')
    player2.computer = True
    player2.name = 'Computron'
    placeAllships(player2)
    gl = OnePlayerGameFunction(player1, player2)
    return gl[-1]


def main():
    print('Welcome to Battleship')
    playerNumbers = playerCountCheck('Please enter the number of players: ')
    if playerNumbers == 0:
        gl = newComputerGame()
        print(f'{gl.get("gameWinner", " ")} won the game '
              f'in {gl.get("offPlayerMoves", " ")} moves')

    elif playerNumbers == 1:
        gl = newOnePlayerGame()
        print(f'{gl.get("gameWinner", " ")} won the '
              f'game in {gl.get("offPlayerMoves", " ")} moves')

        print('1 Player Game')
    elif playerNumbers == 2:
        # TODO 2 Player Function
        print('2 Player Game')


if __name__ == "__main__":
    main()
