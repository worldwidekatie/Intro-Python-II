from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item("Leaf", "Can you believe this lovely fall leaf was just lying on the ground?")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 
[Item("Welcome Mat", "Home Sweet Home. How lovely.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 
[Item("Binoculars", "How else are you supposed to see across such a chasm?")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 
[Item("Treasure Map", "Would've been nice to have that earlier!")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it looks like it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 
[Item("Gold Coin", "I guess they must've dropped this small guy in their treasure-stealing haste!")]),
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

player = Player("Player1", room['outside'], [Item("Pet Rock", "You never leave home without your lucky pet rock!")])

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
print(f"Hello {player.name}! Let's begin...")
print()
print(f"You are currently located at the {player.current_room.name}")
print()
print(player.current_room.description)
print()

while True:
    print("-------------------------------------")
    selection = input("""What would you like to do? 

    To move rooms, enter m
    To check your inventory, enter i
    To look for items in the room, enter l
    To Quit enter q
    """ )

    def room_change():
        print()
        print("-------------------------------------")
        print(f"You're currently in the {player.current_room.name}.")
        print()
        print(player.current_room.description)
        print("-------------------------------------")
        print('\n')

        selection = input("""Which direction would you like to go?

        For North enter n
        For South enter s
        For East enter e
        For West enter w
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
        
        elif selection not in ['n', 's', 'e', 'w']:
            print()
            print("-------------------------------------")
            print("Sorry, that's not a valid command. Try using n, s, e, w, or q.")
            print('\n')
            print(f"You're currently in the {player.current_room.name}.")
            print()
            print(player.current_room.description)
            print("-------------------------------------")
            print('\n')        

        else:
            print()
            print("-------------------------------------")
            print(f"Sorry, that's not a valid direction from the {player.current_room.name}.")
            print()
            print(player.current_room.description)
            print("-------------------------------------")
            print('\n')  

    def inventory():
        print()
        print("-------------------------------------")
        print(f"You have {len(player.items)} item(s) in your bag.")
        print()
        for i in player.items:
            print(f"Item: {i.name}")
            print(f"Description: {i.description}")
            print()
            selection = input("Do you want to drop this item? Enter y or n ") 
            if selection == 'y':
                player.current_room.items.append(i)
                player.items.remove(i)
            print()
        print()
        print("-------------------------------------")
        print(f"You now have {len(player.items)} item(s) in your bag.")
        print('\n')
        print()


    def look_items():
        print()
        print("-------------------------------------")
        print(f"This room has {len(player.current_room.items)} item(s).")
        print()
        for i in player.current_room.items:
            print(f"Item: {i.name}")
            print(f"Description: {i.description}")
            print()
            selection = input("Do you want to pick up this item? Enter y or n ") 
            if selection == 'y':
                player.items.append(i)
                player.current_room.items.remove(i)
            print()
        
        print()
        print("-------------------------------------")
        print(f"You now have {len(player.items)} item(s) in your bag.")
        print(f"There are {len(player.current_room.items)} item(s) left in this room.")
        print('\n')
        print()

    if selection == 'q':
        print("We're sorry to see you go. visit again soon!")
        break
        
    elif selection not in ['m', 'i', 'l', 'q']:
        print()
        print("-------------------------------------")
        print("Sorry, that's not a valid command. Try using m, i, l, or q.")
        print("-------------------------------------")
        print('\n')  
    
    elif selection == 'm':
        room_change()

    elif selection == 'i':
        inventory()
    
    elif selection == 'l':
        look_items()