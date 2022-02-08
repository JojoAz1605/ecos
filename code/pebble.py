import pygame
from code.weapon import Weapon


class Pebble(Weapon):
    def __init__(self, x, y, name, damage):
        super().__init__(x, y, name, damage)
        self.image = pygame.image.load("textures/items/caillou.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey([0, 0, 0])
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)

    def update(self):  # Récupère la position de base
        self.rect.midbottom = self.position
        self.feet.midbottom = self.rect.midbottom
