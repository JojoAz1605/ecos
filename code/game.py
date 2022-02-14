import pygame
import pytmx
import pyscroll
from code.entities.living.humanoid.orc import Orc
from code.entities.living.humanoid.human import Human
from code.pathfinding.utility.grille import Grille
from code.entities.items.pebble import Pebble
from code.entities.items.woodenbranch import Woodenbranch
from code.entities.living.livingentity import LivingEntity
from code.entities.living.animals.rabbit import Rabbit
from code.entities.living.animals.bear import Bear
from code.entities.living.animals.wolf import Wolf
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

        self.grille = Grille(int(self.screen.get_size()[0] / self.TAILLE_CASE),
                             int(self.screen.get_size()[1] / self.TAILLE_CASE))
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
            "items": []
        }
        self.entities["items"].append(Woodenbranch(16 * 4, 16 * 4, "woodenbranch", 20))
        self.entities["items"].append(Pebble(16 * 4, 16 * 16, "pebble", 20))
        for i in range(10):
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

    def nouveau_jour(self) -> None:
        """Fonction qui définit ce qu'il se passe pour un nouveau jour
        """
        if self.day == self.nb_jour_dans_une_annee:  # vérifie si on a atteint le nb de jours dans une année
            for entity_type in self.entities:  # parcours les différentes listes d'entités
                if entity_type == "items":  # si on parcourt la liste des items
                    continue  # on l'ignore
                for entity in self.entities[entity_type]:  # pour toutes les entités dans la liste
                    entity.age += 1  # on incrémente son âge
                    entity.check_life()
                    if not entity.is_alive:  # si l'entité n'est plus vivante
                        self.remove_entity(entity_type, entity)  # on la retire des listes pour qu'elle ne soit plus gérée
            self.day = 0  # on reset le nb de jours
            self.year += 1  # on incrémente l'année
            print(f"Une nouvelle année commence, nous sommes en l'an {self.year} !")
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
        else:
            print(f"ERREUR: L'entité {entity}, n'est pas présente dans la liste")

    def update(self):
        self.nouveau_jour()
        self.group.update()

    def run(self):

        clock = pygame.time.Clock()
        # Fixe le nombre de FPS à chaque tour de boucle pour que le joueur ne se déplace pas trop rapidement

        # Boucle de la simulation

        running = True
        while running:
            for entity_type in self.entities:
                for entity in self.entities[entity_type]:
                    entity.save_location()  # Sauvegarde la position du joueur
            self.update()  # Update la position pour la gestion de collisions
            self.group.draw(self.screen)  # Affiche la map
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Si l'utilisateur clique sur la croix, quitter la fenêtre
            clock.tick(60)  # Fixe le nombre de FPS
        pygame.quit()
