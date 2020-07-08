# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[], lit=True):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items
        self.is_lit = lit

    def take(self, item_name):
        for idx, item in enumerate(self.items):
            if item.name == item_name:
                return self.items.pop(idx)
        return None

    def add_item(self, item):
        self.items.append(item)
