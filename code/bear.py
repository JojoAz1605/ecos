import pygame
from code.player import Player


class Bear(Player):

    def __init__(self, x, y, gender, name, health, attack, age, lifetime, grille):
        super().__init__(x, y, gender, name, health, attack, age, lifetime, grille)
        self.sprite_sheet = pygame.image.load('textures/entities/ours.png')  # Chargement du joueur
        self.image = self.get_image(32, 0)
        # Récupère l'image 0,0 de la decoupe en 32 px, pour avoir l'image 2 de la ligne 1 on va faire 32,0 etc
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir
        self.rect = self.image.get_rect()
        # TODO si quelqu'un veut bien remettre les bons emplacements de sprites, moi je me trompe à chaque fois
        self.images = {
            'down': self.get_image(32, 0),
            'right': self.get_image(32, 32),
            'left': self.get_image(0, 32),
            'up': self.get_image(0, 0)
        }
