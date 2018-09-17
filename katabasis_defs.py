# global constant definitions
GAME_TITLE = R"""
 _   __  ___ _____ ___  ______  ___   _____ _____ _____
| | / / / _ \_   _/ _ \ | ___ \/ _ \ /  ___|_   _/  ___|
| |/ / / /_\ \| |/ /_\ \| |_/ / /_\ \\ `--.  | | \ `--.
|    \ |  _  || ||  _  || ___ \  _  | `--. \ | |  `--. \
| |\  \| | | || || | | || |_/ / | | |/\__/ /_| |_/\__/ /
\_| \_/\_| |_/\_/\_| |_/\____/\_| |_/\____/ \___/\____/

"""

DEBUG_HELP = "enable debug information"

LOAD_HELP = "load a saved game"

DIRS = [['n', 'north'],
        ['e', 'east'],
        ['s', 'south'],
        ['w', 'west']]

ESCAPE = ['q', 'quit', 'exit']

DIRECTIONS = {'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}


# function for parsing room directions
def parse_DIRS(to_parse):
    for row in range(len(DIRS)):
        for elem in range(len(DIRS[row])):
            if to_parse == DIRS[row][elem]:
                return DIRS[row][0]

    return 0


# functtion for parsing game exiting
def parse_ESCAPE(to_parse):
    for elem in ESCAPE:
        if elem == to_parse:
            q = input("Are you sure you want to quit? (y/n) ")
            if q == 'y' or q == 'yes':
                return True

    return False
