import pygame
import pytmx
import pyscroll
from orc import Orc
from human import Human
from myAstar.grille import Grille


class Game:

    def __init__(self):

        # Création de la fenêtre

        self.screen = pygame.display.set_mode((800, 800))
        self.TAILLE_CASE = 16
        pygame.display.set_caption("Ecose - Simulation d'écosystème")

        # Chargement de la carte

        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Définition d'une liste qui va gérer les collisions en stockant les objets tiles de collision

        self.grille = Grille(int(self.screen.get_size()[0] / self.TAILLE_CASE), int(self.screen.get_size()[1] / self.TAILLE_CASE))
        self.walls = []
        for wall in tmx_data.objects:
            if wall.name == "collision":
                newWall = pygame.Rect(wall.x, wall.y, wall.width, wall.height)
                self.walls.append(newWall)
                for point in self.getRectPixels(newWall):
                    self.grille.setVal(point, 1)

        # Générer un joueur

        player_position = tmx_data.get_object_by_name("humain")
        player2_position = tmx_data.get_object_by_name("orc")
        self.player = Human(player_position.x, player_position.y, 0, "Jamie", 100, 10, 0, 50, self.grille)
        self.player2 = Orc(player2_position.x, player2_position.y, 0, "Fred", 100, 10, 0, 50, self.grille)

        # Dessin du groupe de calques

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
        self.group.add(self.player2)

    def touches_input(self):  # Fonction de prise en compte de l'entrée clavier
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player2.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player2.move_down()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player2.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player2.move_right()

    def getRectPixels(self, rect: pygame.Rect):
        posList = []
        for x in range(int(rect.x / self.TAILLE_CASE), int((rect.x + rect.width) / self.TAILLE_CASE)):
            for y in range(int(rect.y / self.TAILLE_CASE), int((rect.y + rect.height) / self.TAILLE_CASE)):
                posList.append((x, y))
        return posList

    def update(self):
        self.group.update()
        # Vérifier la collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_collision()

    def run(self):

        clock = pygame.time.Clock()
        # Fixe le nombre de FPS à chaque tour de boucle pour que le joueur ne se déplace pas trop rapidement

        # Boucle de la simulation

        running = True
        while running:
            self.player2.save_location()
            self.player.save_location()  # Sauvegarde la position du joueur
            self.touches_input()  # Prise en compte de l'entrée clavier
            self.update()  # Update la position pour la gestion de collisions
            self.group.draw(self.screen)  # Affiche la map
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Si l'utilisateur clique sur la croix, quitter la fenêtre
            clock.tick(60)  # Fixe le nombre de FPS
        pygame.quit()
