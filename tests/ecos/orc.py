import pygame
from player import Player


class Orc(Player):

    def __init__(self, x, y, gender, name, health, attack, age, lifetime, grille):
        super().__init__(x, y, gender, name, health, attack, age, lifetime, grille)
        self.weapon = None
        self.sprite_sheet = pygame.image.load('orc.png')  # Chargement du joueur
        self.image = self.get_image(0, 0)
        # Récupère l'image 0,0 de la decoupe en 32 px, pour avoir l'image 2 de la ligne 1 on va faire 32,0 etc
        self.image.set_colorkey([0, 0, 0])  # Couleur de fond en noir
        self.rect = self.image.get_rect()
        self.images = {
            'down': self.get_image(0, 0),
            'right': self.get_image(0, 64),
            'left': self.get_image(0, 32),
            'up': self.get_image(0, 96)
        }

    def player_attack(self, target_player):
        damage = self.attack
        if self.has_weapon():
            damage += self.weapon.damage
        target_player.damage(damage)

    def set_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} a trouvé {self.weapon.name} et gagné {self.weapon.damage} points d'attaque")

    def has_weapon(self):
        return self.weapon is not None