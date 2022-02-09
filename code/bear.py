import pygame
from code.animal import Animal
from random import randint


class Bear(Animal):
    def __init__(self, position, name, gender, world):
        super().__init__(position, name, gender, world)
        self.TYPE = "Bear"
        self.regime = 1
        self.health = 140
        self.attack = 13
        self.age = 0
        self.lifetime = randint(20, 30)

        self.sprite_sheet = pygame.image.load('textures/entities/ours.png')  # Chargement du joueur
        self.image = self.get_image(32, 0)  # Récupère l'image 0,0 de la decoupe en 32 px, pour avoir l'image 2 de la ligne 1 on va faire 32,0 etc
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir
        self.rect = self.image.get_rect()
        self.images = {
            'down': self.get_image(32, 0),
            'right': self.get_image(32, 32),
            'left': self.get_image(0, 32),
            'up': self.get_image(0, 0)
        }
