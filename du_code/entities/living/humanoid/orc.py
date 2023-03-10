from random import randint

import pygame

from du_code.entities.living.humanoid.humanoid import Humanoid


class Orc(Humanoid):
    def __init__(self, position, name, gender, world):
        super().__init__(position, name, gender, world)
        self.type = "orcs"
        self.health = 150
        self.attack = 15
        self.age = 0
        self.lifetime = randint(70, 90)
        self.pregnancy_time = 270  # en jours
        self.eatable = ["humans", "wolves", "rabbits", "bears"]

        self.sprite_sheet = pygame.image.load('textures/entities/orc.png')  # Chargement du joueur
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

    def give_birth(self):
        position_offset = [self.position[0] + self.position[0] % 16, self.position[1] + self.position[1] % 16]
        newChild = Orc(position_offset, self.name + " child", randint(0, 1), self.world)
        self.world.entities["orcs"].add(newChild)
        return newChild
