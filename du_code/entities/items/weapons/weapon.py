from du_code.entities.items.item import Item


class Weapon(Item):
    def __init__(self, position, name, damage):
        super().__init__(position, name)
        self.type = "weapon"
        self.damage = damage

    def get_damage(self):
        return self.damage
