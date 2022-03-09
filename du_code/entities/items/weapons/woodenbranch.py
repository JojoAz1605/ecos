import pygame

from du_code.entities.items.weapons.weapon import Weapon


class Woodenbranch(Weapon):
    def __init__(self, position, name, damage):
        super().__init__(position, name, damage)
        self.image = pygame.image.load("textures/items/baton.png")
