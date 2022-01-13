import pygame
import pytmx
import pyscroll
from player import Player


class Game:

    def __init__(self):

        # Création de la fenêtre

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Ecose - Simulation d'ecosysteme")

        # Chargement de la carte

        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())

        # Définition d'une liste qui va gérer les collisions en stockant les objets tiles de collision

        self.walls = []
        for wall in tmx_data.objects:
            if wall.name == "collision":
                self.walls.append(pygame.Rect(wall.x, wall.y, wall.width, wall.height))

        # Générer un joueur

        player_position = tmx_data.get_object_by_name("humain")
        self.player = Player(player_position.x, player_position.y)

        # Dessin du groupe de calques

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def touches_input(self):  # Fonction de prise en compte de l'entrée clavier
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()

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
