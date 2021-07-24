def generateXaxis():
    """Creates a list for the x axis of 1-10

    Returns:
        LIST: Contains range from 1 - 10
    """
    x_axis = [i for i in range(1, 11)]
    return x_axis


def generateYaxis():
    """Creates a list for the y axis of the letters A-J

    Returns:
        LIST: Contains range from A-J
    """
    y_axis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    return y_axis


def generateBoard():
    """Generates a dictionary which represents a blank battleship board

    Returns:
        DICT: A dictionary that represents the battleship board
    """
    board = {}
    x_axis = generateXaxis()
    y_axis = generateYaxis()
    for y in y_axis:
        for x in x_axis:
            pos = f'{y}:{x}'
            board[pos] = '0'
    return board


def clean_board(shipDict):
    """Takes the given dictionary and replaces the 0 values with a single
    white space.  This is to show a clean looking board

    Args:
        shipDict (DICT): A dictionary representing the battleship board

    Returns:
        DICT: A dictionary where all the 0 values have been replaced with
        a single white space.
    """
    for key, value in shipDict.items():
        if value == '0':
            shipDict[key] = ' '
    return shipDict


def print_hunt_board(ship_dict):
    """Will print the given dictionary in an easy to read format.

    Args:
        ship_dict (DICT): Dictionary representing the battleship board
    """
    ship_dict = clean_board(ship_dict)
    print('    1   2   3   4   5   6   7   8   9   10')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'A | {ship_dict.get("A:1", " ")} | {ship_dict.get("A:2", " ")} | {ship_dict.get("A:3", " ")} | {ship_dict.get("A:4", " ")} | {ship_dict.get("A:5", " ")} | {ship_dict.get("A:6", " ")} | {ship_dict.get("A:7", " ")} | {ship_dict.get("A:8", " ")} | {ship_dict.get("A:9", " ")} | {ship_dict.get("A:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'B | {ship_dict.get("B:1", " ")} | {ship_dict.get("B:2", " ")} | {ship_dict.get("B:3", " ")} | {ship_dict.get("B:4", " ")} | {ship_dict.get("B:5", " ")} | {ship_dict.get("B:6", " ")} | {ship_dict.get("B:7", " ")} | {ship_dict.get("B:8", " ")} | {ship_dict.get("B:9", " ")} | {ship_dict.get("B:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'C | {ship_dict.get("C:1", " ")} | {ship_dict.get("C:2", " ")} | {ship_dict.get("C:3", " ")} | {ship_dict.get("C:4", " ")} | {ship_dict.get("C:5", " ")} | {ship_dict.get("C:6", " ")} | {ship_dict.get("C:7", " ")} | {ship_dict.get("C:8", " ")} | {ship_dict.get("C:9", " ")} | {ship_dict.get("C:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'D | {ship_dict.get("D:1", " ")} | {ship_dict.get("D:2", " ")} | {ship_dict.get("D:3", " ")} | {ship_dict.get("D:4", " ")} | {ship_dict.get("D:5", " ")} | {ship_dict.get("D:6", " ")} | {ship_dict.get("D:7", " ")} | {ship_dict.get("D:8", " ")} | {ship_dict.get("D:9", " ")} | {ship_dict.get("D:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'E | {ship_dict.get("E:1", " ")} | {ship_dict.get("E:2", " ")} | {ship_dict.get("E:3", " ")} | {ship_dict.get("E:4", " ")} | {ship_dict.get("E:5", " ")} | {ship_dict.get("E:6", " ")} | {ship_dict.get("E:7", " ")} | {ship_dict.get("E:8", " ")} | {ship_dict.get("E:9", " ")} | {ship_dict.get("E:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'F | {ship_dict.get("F:1", " ")} | {ship_dict.get("F:2", " ")} | {ship_dict.get("F:3", " ")} | {ship_dict.get("F:4", " ")} | {ship_dict.get("F:5", " ")} | {ship_dict.get("F:6", " ")} | {ship_dict.get("F:7", " ")} | {ship_dict.get("F:8", " ")} | {ship_dict.get("F:9", " ")} | {ship_dict.get("F:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'G | {ship_dict.get("G:1", " ")} | {ship_dict.get("G:2", " ")} | {ship_dict.get("G:3", " ")} | {ship_dict.get("G:4", " ")} | {ship_dict.get("G:5", " ")} | {ship_dict.get("G:6", " ")} | {ship_dict.get("G:7", " ")} | {ship_dict.get("G:8", " ")} | {ship_dict.get("G:9", " ")} | {ship_dict.get("G:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'H | {ship_dict.get("H:1", " ")} | {ship_dict.get("H:2", " ")} | {ship_dict.get("H:3", " ")} | {ship_dict.get("H:4", " ")} | {ship_dict.get("H:5", " ")} | {ship_dict.get("H:6", " ")} | {ship_dict.get("H:7", " ")} | {ship_dict.get("H:8", " ")} | {ship_dict.get("H:9", " ")} | {ship_dict.get("H:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'I | {ship_dict.get("I:1", " ")} | {ship_dict.get("I:2", " ")} | {ship_dict.get("I:3", " ")} | {ship_dict.get("I:4", " ")} | {ship_dict.get("I:5", " ")} | {ship_dict.get("I:6", " ")} | {ship_dict.get("I:7", " ")} | {ship_dict.get("I:8", " ")} | {ship_dict.get("I:9", " ")} | {ship_dict.get("I:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print(f'J | {ship_dict.get("J:1", " ")} | {ship_dict.get("J:2", " ")} | {ship_dict.get("J:3", " ")} | {ship_dict.get("J:4", " ")} | {ship_dict.get("J:5", " ")} | {ship_dict.get("J:6", " ")} | {ship_dict.get("J:7", " ")} | {ship_dict.get("J:8", " ")} | {ship_dict.get("J:9", " ")} | {ship_dict.get("J:10", " ")} |')
    print('   --- --- --- --- --- --- --- --- --- ---')


def print_empty_board():
    """prints a blank battleship board
    """
    print('    1   2   3   4   5   6   7   8   9   10')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('A |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('B |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('C |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('D |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('E |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('F |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('G |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('H |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('I |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')
    print('J |   |   |   |   |   |   |   |   |   |   |')
    print('   --- --- --- --- --- --- --- --- --- ---')

def print_prob_board(ship_dict):
    """Will print the given dictionary in an easy to read format.  Larger in
    format to allow for double digit numbers to be shown correctly.

    Args:
        ship_dict (DICT): Dictionary representing the battleship board
    """
    ship_dict = clean_board(ship_dict)
    print('     1      2      3      4      5      6      7      8      9     10')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'A |  {ship_dict.get("A:1", " ")}  |  {ship_dict.get("A:2", " ")}  |  {ship_dict.get("A:3", " ")}  |  {ship_dict.get("A:4", " ")}  |  {ship_dict.get("A:5", " ")}  |  {ship_dict.get("A:6", " ")}  |  {ship_dict.get("A:7", " ")}  |  {ship_dict.get("A:8", " ")}  |  {ship_dict.get("A:9", " ")}  |  {ship_dict.get("A:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'B |  {ship_dict.get("B:1", " ")}  |  {ship_dict.get("B:2", " ")}  |  {ship_dict.get("B:3", " ")}  |  {ship_dict.get("B:4", " ")}  |  {ship_dict.get("B:5", " ")}  |  {ship_dict.get("B:6", " ")}  |  {ship_dict.get("B:7", " ")}  |  {ship_dict.get("B:8", " ")}  |  {ship_dict.get("B:9", " ")}  |  {ship_dict.get("B:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'C |  {ship_dict.get("C:1", " ")}  |  {ship_dict.get("C:2", " ")}  |  {ship_dict.get("C:3", " ")}  |  {ship_dict.get("C:4", " ")}  |  {ship_dict.get("C:5", " ")}  |  {ship_dict.get("C:6", " ")}  |  {ship_dict.get("C:7", " ")}  |  {ship_dict.get("C:8", " ")}  |  {ship_dict.get("C:9", " ")}  |  {ship_dict.get("C:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'D |  {ship_dict.get("D:1", " ")}  |  {ship_dict.get("D:2", " ")}  |  {ship_dict.get("D:3", " ")}  |  {ship_dict.get("D:4", " ")}  |  {ship_dict.get("D:5", " ")}  |  {ship_dict.get("D:6", " ")}  |  {ship_dict.get("D:7", " ")}  |  {ship_dict.get("D:8", " ")}  |  {ship_dict.get("D:9", " ")}  |  {ship_dict.get("D:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'E |  {ship_dict.get("E:1", " ")}  |  {ship_dict.get("E:2", " ")}  |  {ship_dict.get("E:3", " ")}  |  {ship_dict.get("E:4", " ")}  |  {ship_dict.get("E:5", " ")}  |  {ship_dict.get("E:6", " ")}  |  {ship_dict.get("E:7", " ")}  |  {ship_dict.get("E:8", " ")}  |  {ship_dict.get("E:9", " ")}  |  {ship_dict.get("E:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'F |  {ship_dict.get("F:1", " ")}  |  {ship_dict.get("F:2", " ")}  |  {ship_dict.get("F:3", " ")}  |  {ship_dict.get("F:4", " ")}  |  {ship_dict.get("F:5", " ")}  |  {ship_dict.get("F:6", " ")}  |  {ship_dict.get("F:7", " ")}  |  {ship_dict.get("F:8", " ")}  |  {ship_dict.get("F:9", " ")}  |  {ship_dict.get("F:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'G |  {ship_dict.get("G:1", " ")}  |  {ship_dict.get("G:2", " ")}  |  {ship_dict.get("G:3", " ")}  |  {ship_dict.get("G:4", " ")}  |  {ship_dict.get("G:5", " ")}  |  {ship_dict.get("G:6", " ")}  |  {ship_dict.get("G:7", " ")}  |  {ship_dict.get("G:8", " ")}  |  {ship_dict.get("G:9", " ")}  |  {ship_dict.get("G:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'H |  {ship_dict.get("H:1", " ")}  |  {ship_dict.get("H:2", " ")}  |  {ship_dict.get("H:3", " ")}  |  {ship_dict.get("H:4", " ")}  |  {ship_dict.get("H:5", " ")}  |  {ship_dict.get("H:6", " ")}  |  {ship_dict.get("H:7", " ")}  |  {ship_dict.get("H:8", " ")}  |  {ship_dict.get("H:9", " ")}  |  {ship_dict.get("H:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'I |  {ship_dict.get("I:1", " ")}  |  {ship_dict.get("I:2", " ")}  |  {ship_dict.get("I:3", " ")}  |  {ship_dict.get("I:4", " ")}  |  {ship_dict.get("I:5", " ")}  |  {ship_dict.get("I:6", " ")}  |  {ship_dict.get("I:7", " ")}  |  {ship_dict.get("I:8", " ")}  |  {ship_dict.get("I:9", " ")}  |  {ship_dict.get("I:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')
    print(f'J |  {ship_dict.get("J:1", " ")}  |  {ship_dict.get("J:2", " ")}  |  {ship_dict.get("J:3", " ")}  |  {ship_dict.get("J:4", " ")}  |  {ship_dict.get("J:5", " ")}  |  {ship_dict.get("J:6", " ")}  |  {ship_dict.get("J:7", " ")}  |  {ship_dict.get("J:8", " ")}  |  {ship_dict.get("J:9", " ")}  |  {ship_dict.get("J:10", " ")}  |')
    print('   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----')