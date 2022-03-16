from random import randint

import pygame

from du_code.entities.living.animals.animal import Animal


class Fish(Animal):
    def __init__(self, position, name, gender, world):
        super().__init__(position, name, gender, world)
        self.type = "fishes"
        self.health = 20
        self.attack = 0
        self.age = 0
        self.lifetime = randint(6, 8)
        self.recovery_time = 20
        self.pregnancy_time = 15  # en jours
        self.eatable = ["plants"]
        self.age_mini = 5

        self.sprite_sheet = pygame.image.load('textures/entities/poisson.png')  # Chargement du joueur
        self.image = self.get_image(32, 0)  # Récupère l'image 0,0 de la decoupe en 32 px, pour avoir l'image 2 de la ligne 1 on va faire 32,0 etc
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir
        self.rect = self.image.get_rect()
        self.images = {
            'down': self.get_image(1, 3),
            'right': self.get_image(1, 3),
            'left': self.get_image(62, 3),
            'up': self.get_image(62, 3)
        }

    def give_birth(self):
        position_offset = [self.position[0] + self.position[0] % 16, self.position[1] + self.position[1] % 16]
        newChild = Fish(position_offset, self.name + " child", randint(0, 1), self.world)
        self.world.entities["bears"].add(newChild)
        return newChild
