# room description constants
ENTERANCE_DESC = ("You are standing in the entryway to an old monastery. The "
                  "entryway has collapsed. You see doors to the east, south, "
                  "and west.")

CANTEEN_DESC = ("You are standing in what used to be the canteen. You see "
                "doors to the west and south.")

KITCHEN_DESC = "It's a creepy kitchen. You see a door to the north."

FOYER_DESC = ("Looks like it used to be a nice foyer. You see doors to the "
              "east and south.")

LIBRARY_DESC = ("It's a dilapitated library filled will moldy tomes. "
                "A dessicated monk is slumped over a desk. You see doors to "
                "the north and south.")

CHAPEL_DESC = ("A long abandoned chapel, with decaying corpses contorted in a "
               "final, macabre prayer. You see doors to the north and east.")

BARRACKS_DESC = ("A decrepit barracks, where the monks used to sleep. The "
                 "beds look rather uncomfortable. You see a door to the "
                 "west.")

CELLAR_DESC = ("You see a storeroom. There are barrels full of rotting food. "
               "You see a door to the north.")


# class that holds state information for room objects
class Room:

    def __init__(self, name, dirs, desc="A room."):
        self.room_name = name
        self.exits = dirs
        temp = {}
        for e in range(len(dirs)):
            temp.update({dirs[e]: Portal()})
        self.portals = temp
        self.description = desc

    def enter_room(self):
        print(self.description)
        return self

    def get_grid(self):
        for x in range(len(map)):
            for y in range(len(map[x])):
                if map[x][y] == self:
                    return [x, y]

    def go(self, direction):
        for d in self.exits:
            if d == direction:
                return self.portals[d].try_open()
        return False


class Portal:
    description = "A door or something."
    locked = False
    lock_message = "It's locked."

    def try_open(self):
        if self.locked:
            print(self.lock_message)
            return False
        else:
            return True

# empty = Room("empty", None)

# initiallize room objects
enterance = Room("enterance", ["e", "s", "w"], ENTERANCE_DESC)
enterance.portals['s'].locked = True

canteen = Room("canteen", ["w", "s"], CANTEEN_DESC)

kitchen = Room("kitchen", ["n"], KITCHEN_DESC)

foyer = Room("foyer", ["e", "s"], FOYER_DESC)

library = Room("library", ["n", "s"], LIBRARY_DESC)

chapel = Room("chapel", ["n", "e"], CHAPEL_DESC)

barracks = Room("barracks", ["w"], BARRACKS_DESC)

cellar = Room("cellar", ["n"], CELLAR_DESC)

# assign room entities to map grid
map = [[chapel, library, foyer],
       [barracks, cellar, enterance],
       [None, kitchen, canteen]]
