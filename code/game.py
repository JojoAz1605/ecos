import pygame
import pytmx
import pyscroll
from code.orc import Orc
from code.human import Human
from code.pathfinding.utility.grille import Grille
from random import randint


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
        for i in range(100):
            if randint(0, 1) == 1:
                self.entities.append(Human(player_position.x, player_position.y, 0, str(i), 100, 10, 0, 50, self.grille))
            else:
                self.entities.append(Orc(player_position.x, player_position.y, 0, str(i), 100, 10, 0, 50, self.grille))

        # Dessin du groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        for entity in self.entities:
            self.group.add(entity)

    def getRectPixels(self, rect: pygame.Rect):
        posList = []
        for x in range(int(rect.x / self.TAILLE_CASE), int((rect.x + rect.width) / self.TAILLE_CASE)):
            for y in range(int(rect.y / self.TAILLE_CASE), int((rect.y + rect.height) / self.TAILLE_CASE)):
                posList.append((x, y))
        return posList

    def update(self):
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
            clock.tick(600)  # Fixe le nombre de FPS
        pygame.quit()
