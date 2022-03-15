from random import randint

import pygame

from du_code.brain import Brain


class LivingEntity(pygame.sprite.Sprite):
    def __init__(self, position: list[int, int], name: str,  gender: int, world):
        super().__init__()
        self.type = "Living entity"
        self.position = position
        self.oldposition = self.position.copy()
        self.name = name
        self.gender = gender
        self.world = world
        self.health = int
        self.attack = int
        self.age = int
        self.lifetime = int
        self.grille = world.grille
        self.brain = Brain(self)
        self.pregnant = {"is_pregnant": False, "time_pregnant": 0, "recovery_time": 365}
        self.eatable = list[str]
        self.pregnancy_time = -1
        self.age_mini = -1

        self.sprite_sheet = pygame.image.load('textures/entities/placeholder.png')  # Chargement du joueur
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

    def can_attack(self) -> bool:
        for entity_type in self.eatable:
            entity_group = self.world.entities[entity_type]
            if pygame.sprite.spritecollide(self, entity_group, False):
                for entity in entity_group:
                    if self.rect.colliderect(entity):
                        return True
        return False

    def check_attack(self):
        if self.can_attack() and randint(0, 3) == 0:
            self.entity_attack(self.world.return_closest_entity(self, self.eatable))

    def can_reproduce(self) -> bool:
        entity_group = self.world.entities[self.type]
        if self.gender == 1 and self.world.year >= 1 and pygame.sprite.spritecollide(self, entity_group, False) and len(self.world.entities[self.type]) < 20:
            for entity in entity_group:
                if self.rect.colliderect(entity.rect) and entity.gender != self.gender and entity.age >= entity.age_mini:
                    return True
        return False

    def __str__(self):
        return f"Type: {self.type}; Name: {self.name}; gender: {self.gender}"

    def save_location(self):
        self.oldposition = list(self.position).copy()

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

    def die(self) -> None:
        """Ce qu'il se passe à la mort d'une entité"""
        print(f"\tHO MON DIEU, {self.name}, un {self.type} vient de mourir, c'était un/e {self.gender} :'O")
        self.world.remove_entity(self.type, self)

    def check_life(self) -> None:
        """Check si oui ou non l'entité est morte"""
        if self.health <= 0 or self.age == self.lifetime:
            self.die()

    def update(self):  # Récupère la position de base
        self.check_pregnant()
        self.check_attack()
        self.check_life()
        self.rect.midbottom = self.position
        self.feet.midbottom = self.rect.midbottom
        if self.brain is not None:
            self.brain.do_next_move()  # demande au cerveau de donner le prochain mouvement

    def get_image(self, x, y):  # Fonction pour retourner la map avec les sprites
        image = pygame.Surface([32, 32])  # Le perso fait 32x32
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    def get_all(self):
        return (self.name, self.gender, self.health, self.attack, self.age, self.lifetime)

    def set_all(self, name, gender, health, attack, age, lifetime):
        self.age = age
        self.gender = gender
        self.name = name
        self.health = health
        self.attack = attack
        self.lifetime = lifetime

    def give_birth(self):
        """Créé une nouvelle créature
        :return: la nouvelle créature
        """
        position_offset = [self.position[0] + self.position[0] % 16, self.position[1] + self.position[1] % 16]  # sert pour bien placer le nouveau-né sur la grille
        newChild = LivingEntity(position_offset, self.name + " child", randint(0, 1), self.world)  # créer une nouvelle créature
        self.world.entities[None].add(newChild)  # la rajoute à la liste des entités de son type
        return newChild  # retourne le nouveau-né

    def check_pregnant(self) -> None:
        """Check si une créature est enceinte, et si elle est prête à mettre bas"""
        if self.pregnant["is_pregnant"] and self.pregnant["time_pregnant"] == self.pregnancy_time:  # si la créature est enceinte et qu'elle est prête à mettre bas
            new_child = self.give_birth()  # une naissance
            self.world.group.add(new_child)  # on l'ajoute au groupe
            print(f"\t{self.name}, a donné naissance !")
            self.pregnant["is_pregnant"] = False  # la créature n'est plus enceinte
            self.pregnant["time_pregnant"] = 0
            self.pregnant["recovery_time"] = 365
        elif self.can_reproduce() and not self.pregnant["is_pregnant"] and self.pregnant["recovery_time"] <= 0:
            print(f"\tCHAMPAAAAGNE, {self.name} est enceinte")
            self.pregnant["is_pregnant"] = True
        elif self.pregnant["recovery_time"] != 0:
            self.pregnant["recovery_time"] -= 1
        elif self.pregnant["is_pregnant"]:  # si la créature est enceinte, mais qu'elle n'est pas encore prête à mettre bas
            self.pregnant["time_pregnant"] += 1  # un jour de plus au compteur

    def damage(self, damage):
        self.health -= damage
        print(f"\tAie, {self.name} vient de subir {damage} dégâts et possède maintenant {self.health} points de vie")

    def entity_attack(self, target_player):
        if target_player is not None and target_player.type != "weapons":
            target_player.damage(self.attack)
