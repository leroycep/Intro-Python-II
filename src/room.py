# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def take(self, item_name):
        for idx, item in enumerate(self.items):
            if item.name == item_name:
                return self.items.pop(idx)
        return None
