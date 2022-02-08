import pygame.sprite


class Weapon(pygame.sprite.Sprite):

    def __init__(self, x, y, name, damage):
        super().__init__()
        self.name = name
        self.damage = damage
        self.position = [x, y]
        self.oldposition = self.position.copy()

    def save_location(self):
        self.oldposition = self.position.copy()

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage
