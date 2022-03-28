from typing import Type

from du_code.entities.items.item import Item


class Weapon(Item):
    def __init__(self, position: tuple[int, int], name: str):
        super().__init__(position, name)
        self.type = "weapon"
        self.damage = Type[int]

    def get_damage(self) -> int:
        return self.damage
