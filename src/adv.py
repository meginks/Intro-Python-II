from room import Room
from player import Player
from item import Item
import sys

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
to north. The smell of gold permeates the air."""),

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
room['outside'].s_to = room['narrow']


#
# Main
#

item = {
    'sword': Item('sword', 'for slicing'),
    'dagger': Item('dagger', 'for when you are feeling stabby'),
    'cup': Item('cup', 'for drinking'),
    'book': Item('book', 'for reading'),
    'cloak': Item('cloak', 'for looking stylish'),
    'armor': Item('armor', 'for protecting your body'),
    'coin': Item('coin', 'for paying off debts')
} 

print(item)

room['outside'].items.append(item['armor'])
room['foyer'].items.append(item['cup'])
room['overlook'].items.append(item['dagger']) 
room['treasure'].items.append(item['coin'])
room['narrow'].items.append(item['book'])
room['foyer'].items.append(item['sword'])


# Make a new player object that is currently in the 'outside' room.
player = Player('outside') 
player.room = room['outside']
player.items.append(item['cloak'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(player)
for value in room.values():
    direction = input("""What do you want to do? \n Travel (N)orth, (E)ast, (W)est (S)outh. \n Check (I)nventory \n Explore (R)oom \n (Q)uit. """)
    if direction == "N": 
       player.room = player.room.n_to
    elif direction == "E": 
        player.room = player.room.e_to 
    elif direction == "W":
        player.room = player.room.w_to
    elif direction == "S":
        player.room = player.room.s_to
    elif direction == "I":
        if player.items is None:
            print("You don't have any items")
        elif len(player.items) > 0:
            answer = input(f"You have {player.items}. Drop an item? (Y)es (N)o ").lower().strip()
            if answer == 'y':
                dropped_item = input("What item do you want to drop? ").lower().strip()
                if dropped_item in player.items: 
                    player.items.remove(dropped_item)
            elif answer == 'n':
                break
    elif direction == "R": 
        print(player.room.items)
    elif direction == "Q":
        quit()
    else:
        direction = input("""Invalid input. What do you want to do? \n Travel (N)orth, (E)ast, (W)est (S)outh. \n Check (I)nventory \n Explore (R)oom \n (Q)uit.""").lower().strip() 
    print(player)

