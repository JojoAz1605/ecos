from random import randint

import pygame

from du_code.entities.living.animals.animal import Animal


class Rabbit(Animal):
    def __init__(self, position, name, gender, world):
        super().__init__(position, name, gender, world)
        self.type = "rabbits"
        self.health = 45
        self.attack = 2
        self.age = 0
        self.lifetime = randint(9, 14)
        self.recovery_time = 15
        self.pregnancy_time = 25  # en jours
        self.eatable = ["plants"]
        self.age_mini = 2

        self.sprite_sheet = pygame.image.load('textures/entities/rabbit.png')  # Chargement du joueur
        self.image = self.get_image(32, 0)  # Récupère l'image 0,0 de la decoupe en 32 px, pour avoir l'image 2 de la ligne 1 on va faire 32,0 etc
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir
        self.rect = self.image.get_rect()
        self.images = {
            'down': self.get_image(43, 3),
            'right': self.get_image(45, 37),
            'left': self.get_image(6, 37),
            'up': self.get_image(8, 5)
        }

    def give_birth(self):
        position_offset = [self.position[0] + self.position[0] % 16, self.position[1] + self.position[1] % 16]
        newChild = Rabbit(position_offset, self.name + " child", randint(0, 1), self.world)
        self.world.entities["rabbits"].add(newChild)
        return newChild
