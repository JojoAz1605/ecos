import pygame
import pyscroll
import pytmx

from random import randint
from code.entities.items.pebble import Pebble
from code.entities.items.woodenbranch import Woodenbranch
from code.entities.living.animals.bear import Bear
from code.entities.living.animals.rabbit import Rabbit
from code.entities.living.animals.wolf import Wolf
from code.entities.living.humanoid.human import Human
from code.entities.living.humanoid.orc import Orc
from code.pathfinding.utility.grille import Grille


class Game:

    def __init__(self):

        # Création de la fenêtre

        self.screen = pygame.display.set_mode((800, 800))
        self.TAILLE_CASE = 16
        pygame.display.set_caption("Ecose - Simulation d'écosystème")

        # Chargement de la carte

        tmx_data = pytmx.util_pygame.load_pygame('maps/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Définition d'une liste qui va gérer les collisions en stockant les objets tiles de collision

        self.grille = Grille(int(self.screen.get_size()[0] / self.TAILLE_CASE), int(self.screen.get_size()[1] / self.TAILLE_CASE))
        self.walls = []
        for wall in tmx_data.objects:
            if wall.name == "collision":
                self.walls.append(pygame.Rect(wall.x, wall.y, wall.width, wall.height))
                for point in self.getRectPixels(self.walls[-1]):
                    self.grille.set_val(point, 1)

        # Générer un joueur

        player_position = tmx_data.get_object_by_name("humain")
        self.entities = []
        self.items = []
        self.items.append(Woodenbranch(16*4, 16*4, "woodenbranch", 20))
        self.items.append(Pebble(16*4, 16*16, "pebble", 20))
        for i in range(10):
            entity_type = randint(0, 4)
            entity_name = str(i)
            gender = randint(0, 1)
            if entity_type == 0:
                self.entities.append(Human([player_position.x, player_position.y], entity_name, gender, self))
            elif entity_type == 1:
                self.entities.append(Orc([player_position.x, player_position.y], entity_name, gender, self))
            elif entity_type == 2:
                self.entities.append(Rabbit([player_position.x, player_position.y], entity_name, gender, self))
            elif entity_type == 3:
                self.entities.append(Bear([player_position.x, player_position.y], entity_name, gender, self))
            elif entity_type == 4:
                self.entities.append(Wolf([player_position.x, player_position.y], entity_name, gender, self))

        # Dessin du groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        for entity in self.entities:
            self.group.add(entity)
        for item in self.items:
            self.group.add(item)
        self.day = 0
        self.year = 0

    def getRectPixels(self, rect: pygame.Rect):
        posList = []
        for x in range(int(rect.x / self.TAILLE_CASE), int((rect.x + rect.width) / self.TAILLE_CASE)):
            for y in range(int(rect.y / self.TAILLE_CASE), int((rect.y + rect.height) / self.TAILLE_CASE)):
                posList.append((x, y))
        return posList

    def nouveau_jour(self):
        if self.day == 365:  # à modifier pour changer le rythme de passage des années
            for entity in self.entities:
                entity.age += 1
                if not entity.is_alive:
                    self.entities.remove(entity)
                    self.group.remove(entity)
            self.day = 0
            self.year += 1
            print(f"Une nouvelle année commence, nous sommes en l'an {self.year} !")
        else:
            self.day += 1

    def update(self):
        self.nouveau_jour()
        self.group.update()

    def run(self):

        clock = pygame.time.Clock()
        # Fixe le nombre de FPS à chaque tour de boucle pour que le joueur ne se déplace pas trop rapidement

        # Boucle de la simulation

        running = True
        while running:
            for entity in self.entities:
                entity.save_location()  # Sauvegarde la position du joueur
            self.update()  # Update la position pour la gestion de collisions
            self.group.draw(self.screen)  # Affiche la map
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Si l'utilisateur clique sur la croix, quitter la fenêtre
            clock.tick(60)  # Fixe le nombre de FPS
        pygame.quit()
