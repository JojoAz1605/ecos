import pygame

from du_code.entities.items.weapons.weapon import Weapon


class Pebble(Weapon):
    def __init__(self, position: tuple[int, int], name: str):
        super().__init__(position, name)
        self.image = pygame.image.load("textures/items/caillou.png")
        self.damage = 10
