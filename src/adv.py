import time
import textwrap

from colorama import Fore, Style, Back
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
    'skeletons': Item('skeletons', 'dead stuff')
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

# Place items in rooms

room['foyer'].items.append(item['watch'])
room['foyer'].items.append(item['glasses'])
room['overlook'].items.append(item['pen'])
room['narrow'].items.append(item['computer'])
room['treasure'].items.append(item['skeletons'])

# Main
# Style - commands = white, options = magenta, info = cyan

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Daniel', 'Outside Cave Entrance')
print(f'{Fore.CYAN}Hi, {player1.name}! {Style.RESET_ALL}')
# time.sleep(2)
print(Fore.WHITE + 'Follow the prompts to get to the treasure room, be sure to pick up any items along the way' + Style.RESET_ALL)
print()
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
            print(f'{Fore.CYAN}Current description - {room[i].description}')
            print()
            print('Which way would you like to go?')
            print('Here are your options' + Style.RESET_ALL)
            print()
            for x in ['n_to', 's_to', 'e_to', 'w_to']:
                d = getattr(room[i], x, False)
                button = x.split('_')[0]
                if(d is not False):
                    print(f'{Fore.MAGENTA}For {d.name} press [{button}], {d.name} description - {d.description}{Style.RESET_ALL}')
                    print()
            return room[i]

def move_player(cr, move):
    m = move + '_to'
    d = getattr(cr, m)
    player1.current_room = d.name
    print()
    print(f'{Fore.CYAN}{player1.name}! is now in the {player1.current_room}{Style.RESET_ALL}')
    done = False
    while done == False:
        done = get_drop_items(d)
    return player1

def get_drop_items(d):
    if(len(d.items) > 0):
        print()
        print(f'{Fore.CYAN}The {d.name} has the following items')
        for i in d.items:
            print(i.name)
        print()
        get = input(Fore.WHITE + 'If you want to pick up an item (you can only pick up one item per visit), type [y] [item name], otherwise type [n]').split()
        print()
        if get[0] == 'y':
            player1.pick_up_item(item[get[1]])
            d.remove_item(item[get[1]])
            time.sleep(2)
            print()

    if(len(player1.itemsBag) > 0):
        print()
        print(f'{Fore.CYAN}You have the following items in your bag')
        for i in player1.itemsBag:
            print(i.name)
        print()
        drop = input(Fore.WHITE + 'If you want to drop an item, type [y] [item name] otherwise type [n]').split()
        print()
        if drop[0] == 'y':
            player1.drop_item(item[drop[1]])
            d.add_item(item[drop[1]])
            time.sleep(2)
            print()
            return True
        else:
            return True

def game():
    found_treasure_room = False
    while found_treasure_room is False:
        current_room = find_room_and_options()
        move = input(Fore.WHITE + 'Enter the direction you would like to go, [n] [s] [e] or [w]' + Style.RESET_ALL)
        player = move_player(current_room, move)
        if(player.current_room == 'Treasure Chamber'):
            found_treasure_room = True

# Start of game
print(f'{Fore.CYAN}Current place - {player1.current_room}{Style.RESET_ALL}')
game()
print()
print(f'{Fore.YELLOW}Congrats {player1.name}! You found the treasure room!')
print()