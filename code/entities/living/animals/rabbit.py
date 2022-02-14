from random import randint

import pygame

from code.entities.living.animals.animal import Animal


class Rabbit(Animal):
    def __init__(self, position, name, gender, world):
        super().__init__(position, name, gender, world)
        self.type = "Rabbit"
        self.health = 20
        self.attack = 2
        self.age = 0
        self.lifetime = randint(9, 14)
        self.pregnancy_time = 31  # en jours
        self.eatable = ["plants"]  # TODO des plantes parce que povr piti lapain i peu pa mangé

        self.sprite_sheet = pygame.image.load('textures/entities/rabbit.png')  # Chargement du joueur
        self.image = self.get_image(32, 0)  # Récupère l'image 0,0 de la decoupe en 32 px, pour avoir l'image 2 de la ligne 1 on va faire 32,0 etc
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir
        self.rect = self.image.get_rect()
        self.images = {
            'down': self.get_image(32, 0),
            'right': self.get_image(32, 32),
            'left': self.get_image(0, 32),
            'up': self.get_image(0, 0)
        }

    def give_birth(self):
        position_offset = [self.position[0] + self.position[0] % 16, self.position[1] + self.position[1] % 16]
        newChild = Rabbit(position_offset, self.name + " child", randint(0, 1), self.world)
        self.world.entities["rabbits"].append(newChild)
        return newChild
