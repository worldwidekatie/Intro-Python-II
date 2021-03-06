from room import Room
from player import Player
#from item import Item

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Player1", room['outside'])

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
print('\n')
print('--------------------------------------')
selection = input("""Welcome to The Game new adventurer. 

What is your name? """)
player.name = selection
print('--------------------------------------')
print('\n')
print('--------------------------------------')
print()
print(f"Hello {player.name}! Let's begin...")
print()
print(f"You are currently {player.current_room.name}")
print()
print(player.current_room.description)
print()

while True:
    print("-------------------------------------")
    selection = input("""Which direction would you like to go?

    For North enter n
    For South enter s
    For East enter e
    For West enter w
    To Quit enter q
    """ )

    def change_room():
        print()
        print("-------------------------------------")
        print(f"Welcome to the {player.current_room.name}!")
        print()
        print(player.current_room.description)
        print("-------------------------------------")
        print('\n')

    if selection == 'n' and player.current_room.n_to != 'none':
        player.current_room = player.current_room.n_to
        change_room()

    elif selection == 's' and player.current_room.s_to != 'none':
        player.current_room = player.current_room.s_to
        change_room()

    elif selection == 'e' and player.current_room.e_to != 'none':
        player.current_room = player.current_room.e_to
        change_room()

    elif selection == 'w' and player.current_room.w_to != 'none':
        player.current_room = player.current_room.w_to
        change_room()

    elif selection == 'q':
        print("We're sorry to see you go. visit again soon!")
        break
    
    elif selection not in ['n', 's', 'e', 'w', 'q']:
        print("Sorry, that's not a valid command. Try using n, s, e, w, or q.")

    else:
        print("Sorry, that's not a valid direction. Try going a different direction.")


 
 