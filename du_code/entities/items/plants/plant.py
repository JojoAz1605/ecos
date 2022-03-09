from du_code.entities.items.item import Item


class Plant(Item):
    def __init__(self, position, name, world):
        super(Plant, self).__init__(position, name)
        self.world = world
        self.type = "plants"

    def damage(self, damage):
        print(f"OOF, {self.name} a été mangé(e)")
        self.world.remove_entity(self.type, self)
