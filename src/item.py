class Item:
    def __init__(self, name, description, provides_light=False):
        self.name = name
        self.description = description
        self.provides_light = provides_light

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description, provides_light=True)

    def on_drop(self):
        print(f"It's not wise to drop your {self.name}")
