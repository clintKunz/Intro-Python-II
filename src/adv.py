import time
import textwrap

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
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all the items

item = {
    'glasses': Item('glasses', 'helps you see'),

    'watch': Item('watch', 'tells time'),

    'computer': Item('computer', 'can do all sorts of things'),

    'pen': Item('pen', 'writes poetry'),

    'treasure box': Item('treasure box', 'a box full of gold')
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
player1 = Player('Daniel', 'Outside Cave Entrance')
print(f'Hi, {player1.name}!')
# time.sleep(2)
print('Follow the prompts to get to the treasure room to find the treasure box')
# time.sleep(2)

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def find_room_and_options():
    for i in room:
        if player1.current_room == room[i].name:
            print(f'Current description - {room[i].description}')
            print('Which way would you like to go?')
            print('Here are your options')
            for x in ['n_to', 's_to', 'e_to', 'w_to']:
                d = getattr(room[i], x, False)
                button = x.split('_')[0]
                if(d is not False):
                    print(f'For {d.name} press [{button}], {d.description}')

print(f'Current place - {player1.current_room}')
# find_room_and_options()
move = input('Enter the direction you would like to go, [n] [s] [e] or [w]')
print(move)