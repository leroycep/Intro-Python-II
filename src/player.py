# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room, inventory=[], name=""):
        self.current_room = current_room
        self.inventory = inventory
        self.name = name

    def take(self, item_name):
        for idx, item in enumerate(self.inventory):
            if item.name == item_name:
                return self.inventory.pop(idx)
        return None

    def can_see(self):
        if self.current_room.is_lit:
            return True
        for item in self.current_room.items:
            if item.provides_light:
                return True
        for item in self.inventory:
            if item.provides_light:
                return True
        return False

