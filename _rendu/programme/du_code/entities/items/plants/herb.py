import pygame

from du_code.entities.items.plants.plant import Plant


class Herb(Plant):
    def __init__(self, position, name, world):
        super().__init__(position, name, world)
        self.image = pygame.image.load("textures/items/herbe.png")

