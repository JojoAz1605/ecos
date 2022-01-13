import pygame
from brain import Brain


class Player(pygame.sprite.Sprite):
    # Element graphique du jeu qui peut interargir avec d'autres sprite

    def __init__(self, x, y):
        super().__init__()  # Initialisation du sprite
        self.sprite_sheet = pygame.image.load('player.png')  # Chargement de la map
        self.image = self.get_image(0, 0)
        # Récupère l'image 0,0 de la decoupe en 32 px, pour avoir l'image 2 de la ligne 1 on va faire 32,0 etc
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir
        self.rect = self.image.get_rect()
        self.position = [x, y]  # Récupère la position du joueur
        self.images = {
            'down': self.get_image(0, 0),
            'right': self.get_image(0, 64),
            'left': self.get_image(0, 32),
            'up': self.get_image(0, 96)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)  # Pied du joueur de la taille de la moitié du joueur
        self.oldposition = self.position.copy()  # Copie de la position du joueur avant qu'il ne bouge
        self.brain = Brain(self)  # le cerveau du joueur, il ne fait pas grand-chose pour l'instant

    def save_location(self):
        self.oldposition = self.position.copy()

    def animation(self, name):  # Va chercher l'image à appliquer à l'appui dela touche
        self.image = self.images[name]
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir

    def move_right(self):  # Se déplace de vitesse 2
        self.position[0] += 2
        self.animation('right')

    def move_left(self):
        self.position[0] -= 2
        self.animation('left')

    def move_up(self):
        self.position[1] -= 2
        self.animation('up')

    def move_down(self):
        self.position[1] += 2
        self.animation('down')

    def update(self):  # Récupère la position de base
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom  # Positionner les pieds par rapport au rectangle
        #  self.brain.doNextMove()  # demande au cerveau de donner le prochain mouvement

    def move_collision(self):
        self.position = self.oldposition  # La position reste la position d'avant la collision
        self.rect.topleft = self.position  # Position par rapport au rectangl
        self.feet.midbottom = self.rect.midbottom  # Positionner les pieds par rapport au rectangle

    def get_image(self, x, y):  # Fonction pour retourner la map avec les sprites
        image = pygame.Surface([32, 32])  # Le perso fait 32x32
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
