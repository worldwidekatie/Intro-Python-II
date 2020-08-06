# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
    def __init__(self, name, current_room, items=[Item("Pet Rock", "You never leave home without your lucky pet rock!")]):
        self.name = name
        self.current_room = current_room
        self.items = items