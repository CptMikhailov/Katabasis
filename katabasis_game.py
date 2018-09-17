#!/usr/bin/env python

from katabasis_rooms import *
import katabasis_defs as c
import argparse


# contains main game logic and command parsing functions
class Game:
    game_over = False

    @staticmethod
    def command(s):
        """Takes command-line input and parses it, according to definitions in
           the katabasis_defs.py library."""

        cmd = Game.format(s)

        for i in cmd:

            temp = c.parse_DIRS(i)
            if c.parse_DIRS(i) != 0:
                player.move(temp)
                break

            elif c.parse_ESCAPE(i):
                exit(0)

        else:
            print("Huh?")

    @staticmethod
    def format(s):
        """Takes the command-line input, and strips, lowers, and splits it."""
        s = s.strip()
        s = s.lower()
        formatted = s.split(' ')

        if args.debug:
            print("Formatted input: [", end=' ')
            for i in formatted:
                print(i, end=' ')
            print("]")

        return formatted

    # save game function to be implemented
    @staticmethod
    def save():
        pass


# class that defines character entities
# this is currently limited to the player, but may be extended
# to other entities in the future
class Char:
    def __init__(self, start):
        self.loc = start.enter_room()

    def move(self, direction):
        x, y = self.loc.get_grid()

        if self.loc.go(direction):
            d = c.DIRECTIONS[direction]
            x += d[0]
            y += d[1]
            self.loc = (map[x][y]).enter_room()
        else:
            print("You can't go there.")
        if args.debug:
            print(f"Current location: {self.loc.room_name}")


if __name__ == "__main__":
    # gets command-line arguments and parses them
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help=c.DEBUG_HELP, action='store_true')
    parser.add_argument('-l', metavar='<filename>.sav', help=c.LOAD_HELP)

    args = parser.parse_args()
    if args.debug:
        print("Debug mode enabled.")

    print(c.GAME_TITLE)

    # instantiates player object and sets location to enterance
    player = Char(enterance)

    # begin game loop
    while not Game.game_over:

        # gets player input, then passes it to command parser
        Game.command(input("> "))
