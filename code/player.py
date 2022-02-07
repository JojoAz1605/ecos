import pygame
from code.brain import Brain


class Player(pygame.sprite.Sprite):
    # Element graphique du jeu qui peut interargir avec d'autres sprite

    def __init__(self, x, y, gender, name, health, attack, age, lifetime, grille):
        super().__init__()  # Initialisation du sprite
        self.name = name  # Variable nom
        self.gender = gender  # Variable sexe
        self.age = age  # Variable age
        self.health = health  # Variable vie
        self.attack = attack  # Variable attaque
        self.lifetime = lifetime  # Variable durée de vie
        self.weapon = None  # Variable arme initialisée à None, car il n'a pas d'arme en main au début du jeu
        self.sprite_sheet = pygame.image.load('textures/entities/player.png')  # Chargement du joueur
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
        self.oldposition = self.position.copy()  # Copie de la position du joueur avant qu'il ne bouge
        self.grille = grille
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
        self.rect.midbottom = self.position
        self.brain.doNextMove()  # demande au cerveau de donner le prochain mouvement

    def get_image(self, x, y):  # Fonction pour retourner la map avec les sprites
        image = pygame.Surface([32, 32])  # Le perso fait 32x32
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    def get_all(self):
        return (self.name, self.gender, self.health, self.attack, self.age, self.lifetime)

    def damage(self, damage):
        self.health -= damage
        print(f"Aie, {self.name} vient de subir {damage} dégâts et possède maintenant {self.health} points de vie")

    def set_all(self, name, gender, health, attack, age, lifetime):
        self.age = age
        self.gender = gender
        self.name = name
        self.health = health
        self.attack = attack
        self.lifetime = lifetime

    def player_attack(self, target_player):
        damage = self.attack
        if self.has_weapon():
            damage += self.weapon.damage
        target_player.damage(damage)

    def set_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} a trouvé {self.weapon.name} et gagne {self.weapon.damage} points d'attaque")

    def has_weapon(self):
        return self.weapon is not None
