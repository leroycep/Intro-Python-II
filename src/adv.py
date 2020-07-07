from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("gold", "a nugget of gold")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

def direction_name(direction):
    if direction == 'n':
        return "north"
    elif direction == 'e':
        return "east"
    elif direction == 's':
        return "south"
    elif direction == 'w':
        return "west"

def move_to_room(player, direction):
    next_room = None
    if direction == 'n':
        next_room = player.current_room.n_to
    elif direction == 'e':
        next_room = player.current_room.e_to
    elif direction == 's':
        next_room = player.current_room.s_to
    elif direction == 'w':
        next_room = player.current_room.w_to

    if next_room == None:
        print(f"There is no way to go {direction_name(direction)}")
    else:
        player.current_room = next_room

while True:
    print(f"\n# {player.current_room.name}\n")
    print(f"{player.current_room.description}\n")

    if (len(player.current_room.items) > 0):
        print(f"\n## Items")
    for item in player.current_room.items:
        print(f"- {item.name}: {item.description}")
    if (len(player.current_room.items) > 0):
        print()

    action = None
    try:
        action = input("> ").split(" ")
    except EOFError:
        break

    if action[0] == "quit" or action[0] == "q":
        break
    elif action[0] == "north" or action[0] == "n":
        move_to_room(player, "n")
    elif action[0] == "east" or action[0] == "e":
        move_to_room(player, "e")
    elif action[0] == "south" or action[0] == "s":
        move_to_room(player, "s")
    elif action[0] == "west" or action[0] == "w":
        move_to_room(player, "w")
    elif action[0] == "get":
        if len(action) != 2:
            print("Invalid usage of `get`")
            print("Usage:")
            print(f"  {action[0]} <item>")
            continue
        item = player.current_room.take(action[1])
        if item == None:
            print(f"I don't see a {action[1]} around here")
        else:
            player.inventory.append(item)
    elif action[0] == "inventory" or action[0] == "inv":
        print("# Inventory")
        for item in player.inventory:
            print(f"- {item.name}: {item.description}")
        print()
    else:
        print(f"I don't know how to \"{action[0]}\"")
