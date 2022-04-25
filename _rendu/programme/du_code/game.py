import pygame
import pytmx
import pyscroll
import numpy as np
import matplotlib.pyplot as plt

from du_code.entities.living import livingentity
from du_code.entities.living.humanoid.orc import Orc
from du_code.entities.living.humanoid.human import Human
from du_code.pathfinding.utility.grille import Grille
from du_code.entities.items.weapons.pebble import Pebble
from du_code.entities.items.weapons.woodenbranch import Woodenbranch
from du_code.entities.items.plants.herb import Herb
from du_code.entities.living.livingentity import LivingEntity
from du_code.entities.living.animals.rabbit import Rabbit
from du_code.entities.living.animals.bear import Bear
from du_code.entities.living.animals.wolf import Wolf
from du_code.entities.living.animals.fish import Fish

from random import randint


class Game:
    def __init__(self):
        # Création de la fenêtre
        self.screen = pygame.display.set_mode((1050, 800))
        pygame.display.set_caption("Ecos - Simulation d'écosystème")
        self.TAILLE_CASE = 16

        # Chargement de la carte
        self.tmx_data = pytmx.util_pygame.load_pygame('maps/carte.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())

        # Définition d'une liste qui va gérer les collisions en stockant les objets tiles de collision

        self.grille = Grille(int(self.screen.get_size()[0] / self.TAILLE_CASE), int(self.screen.get_size()[1] / self.TAILLE_CASE))
        self.walls = []
        self.spawn_pos = []  # liste des positions valides en tant que spawn d'entités
        self.generate_collisions()
        self.generate_spawnpoints()
        print(self.spawn_pos)

        # Dessin du groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=3)

        self.entities = {
            "humans": pygame.sprite.Group(),
            "orcs": pygame.sprite.Group(),
            "rabbits": pygame.sprite.Group(),
            "bears": pygame.sprite.Group(),
            "wolves": pygame.sprite.Group(),
            "fishes": pygame.sprite.Group(),
            "plants": pygame.sprite.Group(),
            "weapons": pygame.sprite.Group()
        }
        # ajout d'armes sur la map
        self.entities["weapons"].add(Woodenbranch((16 * 4, 16 * 4), "woodenbranch"))  # ajoute une branche sur la map
        self.entities["weapons"].add(Pebble((16 * 4, 16 * 16), "pebble"))  # ajoute un caillou sur la map

        # ajoute des herbes sur la map(parfois dans l'eau)
        for i in range(5):
            self.entities["plants"].add(Herb((randint(16, 784), randint(16, 784)), "herb1", self))
        self.populate_world(50)  # place les entités sur la carte

        self.day = 0  # le jour actuel
        self.year = 0  # l'année actuelle
        self.nb_jour_dans_une_annee = 365  # à modifier pour changer le rythme de passage des années
        self.entities_counter_array = np.zeros((1, 6), int)
        self.update_array()

    def generate_collisions(self) -> None:
        for wall in self.tmx_data.objects:  # parcours les murs
            if wall.name == "collision":  # si il y a des collisions
                self.walls.append(pygame.Rect(wall.x, wall.y, wall.width, wall.height))  # on ajoute ça à la liste des murs
                for point in self.get_rect_pixels(self.walls[-1]):  # parcours les points du mur
                    self.grille.set_val(point, 1)  # et fait en sorte que cette case soit considérée comme étant un obstacle

    def generate_spawnpoints(self):
        for x in range(0, self.grille.width * 16, 16):
            for y in range(0, self.grille.width * 16, 16):
                possible_rect = pygame.Rect(x, y, 16, 16)
                if [x, y] not in self.spawn_pos and possible_rect.collidelist(self.walls) == -1:
                    self.spawn_pos.append([x, y])

    def populate_world(self, nb_entity: int) -> None:
        """Rajoute des entités dans le monde
        :param nb_entity: le nombre d'entités à rajouter
        """
        # position de base
        player_position = self.tmx_data.get_object_by_name("humain")

        for i in range(nb_entity):  # boucle pour créer des entités
            pos = self.spawn_pos[randint(0, len(self.spawn_pos) - 1)]
            entity_type = randint(0, 4)  # prend un type d'entité aléatoire
            entity_name = str(i)  # le nom, c'est juste un nombre
            gender = randint(0, 1)  # genre aléatoire
            if entity_type == 0:
                self.entities["humans"].add(Human(pos, entity_name, gender, self))
            elif entity_type == 1:
                self.entities["orcs"].add(Orc(pos, entity_name, gender, self))
            elif entity_type == 2:
                self.entities["rabbits"].add(Rabbit(pos, entity_name, gender, self))
            elif entity_type == 3:
                self.entities["bears"].add(Bear(pos, entity_name, gender, self))
            elif entity_type == 4:
                self.entities["wolves"].add(Wolf(pos, entity_name, gender, self))
            elif entity_type == 5:
                self.entities["fishes"].add(Fish(pos, entity_name, gender, self))  # c'est plus une blague qu'autre chose
        for entity_type in self.entities:
            # livingentity.update_animation()
            for entity in self.entities[entity_type]:
                self.group.add(entity)

    def get_rect_pixels(self, rect: pygame.Rect) -> list[tuple[int, int]]:
        """Renvoie la liste des pixels composants un rectangle
        :param rect: un rectangle
        :return: une liste des positions des pixels
        """
        posList = []
        for x in range(int(rect.x / self.TAILLE_CASE), int((rect.x + rect.width) / self.TAILLE_CASE)):
            for y in range(int(rect.y / self.TAILLE_CASE), int((rect.y + rect.height) / self.TAILLE_CASE)):
                posList.append((x, y))
        return posList

    def update_array(self) -> None:
        le_truc_a_rajouter = []
        for entity_type in self.entities:
            if entity_type not in "plantsweapons":
                le_truc_a_rajouter.append(len(self.entities[entity_type]))
        oui = np.array(le_truc_a_rajouter).reshape(1, 6)
        self.entities_counter_array = np.append(self.entities_counter_array, oui, axis=0)

    def make_graph(self) -> None:
        types = ["humans", "orcs", "rabbits", "bears", "wolves", "fishes"]
        x = np.array(range(0, self.year+2))
        for col in range(self.entities_counter_array.shape[1]):
            plt.plot(x, self.entities_counter_array[:, col])
        plt.legend(types, loc="upper left")
        plt.grid(True)
        plt.xlabel("Temps qui passe"), plt.ylabel("Nombres d'entités")
        plt.savefig("graphs/graph")
        plt.close()

    def nouveau_jour(self) -> None:
        """Fonction qui définit ce qu'il se passe pour un nouveau jour
        """
        if self.day == self.nb_jour_dans_une_annee:  # vérifie si on a atteint le nb de jours dans une année
            for entity_type in self.entities:  # parcours les différentes listes d'entités
                if entity_type == "weapons" or entity_type == "plants":  # si on parcourt la liste des items
                    continue  # on l'ignore
                for entity in self.entities[entity_type]:  # pour toutes les entités dans la liste
                    entity.age += 1  # on incrémente son âge
            self.day = 0  # on reset le nb de jours
            self.year += 1  # on incrémente l'année
            self.update_array()
            self.make_graph()
            print(f"\n-----Une nouvelle année commence, nous sommes en l'an {self.year} !-----")
            for entity_type in self.entities:
                if len(self.entities[entity_type]) != 0:
                    print(f"Les {entity_type} sont maintenant {len(self.entities[entity_type])}!", end=', ')
            print()
        else:
            self.day += 1  # on incrémente le jour

    def update(self) -> None:
        self.nouveau_jour()
        self.group.update()

    def run(self) -> None:
        clock = pygame.time.Clock()  # Fixe le nombre de FPS à chaque tour de boucle pour que le joueur ne se déplace pas trop rapidement

        font = pygame.freetype.Font("polices/FreeSansBold.ttf", 24)  # la police qui servira pour l'affichage

        # Boucle de la simulation
        running = True
        while running:
            self.update()  # Update la position pour la gestion de collisions
            self.group.draw(self.screen)  # Affiche la map
            surface_pos_y = 30
            for entity_type in self.entities:
                entity_counter_surface, rect = font.render(f"{entity_type}: {str(len(self.entities[entity_type]))}", (255, 255, 255))  # affichage graphique d'un compteur d'entité
                self.screen.blit(entity_counter_surface, (800, surface_pos_y))  # affichage du compteur
                surface_pos_y += 30  # décale en y
                for entity in self.entities[entity_type]:
                    entity.save_location()  # Sauvegarde la position du joueur
            timer_surface, rect = font.render(f"Année: {str(self.year)} | Jour: {str(self.day)}", (255, 255, 255))  # affichage graphique du timer
            self.screen.blit(timer_surface, (800, 0))  # affichage du timer

            pygame.display.flip()  # poof, affichage == cédela majiiii
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Si l'utilisateur clique sur la croix, quitter la fenêtre
            clock.tick(60)  # Fixe le nombre de FPS
        pygame.quit()  # pouf aplu pygame
