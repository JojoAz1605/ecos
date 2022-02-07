import pygame
from code.weapon import Weapon

class Caillou(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.image = pygame.image.load("textures/items/caillou.png")
        self.rect = self.image.get_rect()
