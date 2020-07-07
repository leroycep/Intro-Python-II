# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room, inventory=[]):
        self.current_room = current_room
        self.inventory = inventory

    def take(self, item_name):
        for idx, item in enumerate(self.inventory):
            if item.name == item_name:
                return self.inventory.pop(idx)
        return None

