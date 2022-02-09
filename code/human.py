from code.humanoid import Humanoid
from random import randint
import pygame


class Human(Humanoid):
    def __init__(self, position, name, gender, world):
        super().__init__(position, name, gender, world)
        self.TYPE = "Human"
        self.health = 100
        self.attack = 10
        self.age = 0
        self.lifetime = randint(60, 85)

        self.sprite_sheet = pygame.image.load('textures/entities/human.png')  # Chargement du joueur
        self.image = self.get_image(0, 0)  # Récupère l'image 0,0 de la decoupe en 32 px, pour avoir l'image 2 de la ligne 1 on va faire 32,0 etc
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)  # pied du joueur de la taille de la moitié du joueur
        self.images = {
            'down': self.get_image(0, 0),
            'right': self.get_image(0, 64),
            'left': self.get_image(0, 32),
            'up': self.get_image(0, 96)
        }
