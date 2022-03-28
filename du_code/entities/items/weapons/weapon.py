from typing import Type

from du_code.entities.items.item import Item


class Weapon(Item):
    def __init__(self, position: tuple[int, int], name: str):
        super().__init__(position, name)
        self.type = "weapon"
        self.damage = Type[int]
        self.cooldown = 0

    def checklist(self):
        self.check_cooldown()

    def check_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def get_damage(self) -> int:
        return self.damage
