import pygame
import pytmx
import pyscroll
import numpy as np
import matplotlib.pyplot as plt

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

from random import randint


class Game:
    def __init__(self):
        # Création de la fenêtre
        self.screen = pygame.display.set_mode((1050, 800))
        pygame.display.set_caption("Ecos - Simulation d'écosystème")
        self.TAILLE_CASE = 16

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
        self.entities = {
            "humans": [],
            "orcs": [],
            "rabbits": [],
            "bears": [],
            "wolves": [],
            "plants": [],
            "weapons": []
        }
        self.entities["weapons"].append(Woodenbranch((16 * 4, 16 * 4), "woodenbranch", 20))  # ajoute une branche sur la map
        self.entities["weapons"].append(Pebble((16 * 4, 16 * 16), "pebble", 20))  # ajoute un caillou sur la map

        for i in range(50):  # ajoute des herbes
            self.entities["plants"].append(Herb((randint(16, 784), randint(16, 784)), "herb1", self))
        for i in range(40):
            entity_type = randint(0, 4)
            entity_name = str(i)
            gender = randint(0, 1)
            if entity_type == 0:
                self.entities["humans"].append(Human([player_position.x, player_position.y], entity_name, gender, self))
            elif entity_type == 1:
                self.entities["orcs"].append(Orc([player_position.x, player_position.y], entity_name, gender, self))
            elif entity_type == 2:
                self.entities["rabbits"].append(Rabbit([player_position.x, player_position.y], entity_name, gender, self))
            elif entity_type == 3:
                self.entities["bears"].append(Bear([player_position.x, player_position.y], entity_name, gender, self))
            elif entity_type == 4:
                self.entities["wolves"].append(Wolf([player_position.x, player_position.y], entity_name, gender, self))

        # Dessin du groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        for entity_type in self.entities:
            for entity in self.entities[entity_type]:
                self.group.add(entity)
        self.day = 0  # le jour actuel
        self.year = 0  # l'année actuelle
        self.nb_jour_dans_une_annee = 365  # à modifier pour changer le rythme de passage des années
        self.entities_counter_array = np.zeros((1, 5), int)
        self.update_array()

    def getRectPixels(self, rect: pygame.Rect) -> list[tuple[int, int]]:
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
        oui = np.array(le_truc_a_rajouter).reshape(1, 5)
        self.entities_counter_array = np.append(self.entities_counter_array, oui, axis=0)

    def make_graph(self) -> None:
        types = ["humans", "orcs", "rabbits", "bears", "wolves"]
        x = np.array(range(0, self.year+2))
        for col in range(self.entities_counter_array.shape[1]):
            plt.plot(x, self.entities_counter_array[:, col])
        plt.legend(types)
        plt.savefig(f"graphs/année - {str(self.year)}")

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

    def remove_entity(self, entity_type: str, entity: LivingEntity) -> None:
        """Retire une entité des listes
        :param entity_type: le type de l'entité à retirer
        :param entity: l'entité à retirer
        """
        if entity in self.entities[entity_type]:  # vérifie que l'entité est présente dans la liste
            self.entities[entity_type].remove(entity)  # on la retire
            self.group.remove(entity)
        entity.kill()

    def get_entities_list(self, entity_types: list[str]) -> list[LivingEntity]:
        res = []
        for entity_type in entity_types:
            if entity_type not in self.entities:
                return res
        for entity_type in entity_types:
            for entity in self.entities[entity_type]:
                res.append(entity)
        return res

    def update(self):
        self.nouveau_jour()
        self.group.update()

    def calculate_dist(self, entity: LivingEntity, another_entity: LivingEntity) -> float:
        """Calcul de distance entre une entité et une autre
        :param entity: une entité
        :param another_entity: une autre entité
        :return: la distance entre les deux
        """
        return abs(another_entity.position[0] - entity.position[0]) + abs(
            another_entity.position[1] - entity.position[1])  # calcul par distance de Manhattan

    def return_closest_entity(self, this_entity: LivingEntity, entity_types: list[LivingEntity]) -> list[LivingEntity]:
        try:
            closest = self.entities[entity_types[0]][0]
            for entity_type in entity_types:
                for entity in self.entities[entity_type]:
                    if self.calculate_dist(this_entity, entity) <= self.calculate_dist(this_entity, closest):
                        closest = entity
            return closest
        except IndexError:
            pass

    def run(self):
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
