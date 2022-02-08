import pygame
from code.weapon import Weapon


class Woodenbranch(Weapon):
    def __init__(self, x, y, name, damage):
        super().__init__(name, damage)
        self.image = pygame.image.load("textures/items/baton.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey([0, 0, 0])
        self.position = [x, y]

    def update(self):  # Récupère la position de base
        self.rect.midbottom = self.position
        self.feet.midbottom = self.rect.midbottom