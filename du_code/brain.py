from random import randint

from du_code.pathfinding.astar import Astar


class Brain:
    def __init__(self, owner):
        """Un cerveau pour une créature
        :param owner: le propriétaire du cerveau
        """
        self.owner = owner
        self.etape = 0  # progression de l'entité vers sa destination
        self.grille = self.owner.grille  # la grille sur laquelle évolue l'entité
        self.path = None  # le chemin initialisé comme étant nul
        self.destination = self.get_random_dest()  # la destination initialisée comme étant aléatoire
        self.algo = Astar(self.grille, (int(self.owner.position[0] / 16), int(self.owner.position[1] / 16)), self.destination)  # l'algorithme permettant de calculer le chemin

    def vec_2_dir(self, vec: tuple[int, int]) -> int:
        """
        :param vec: un vecteur de direction
        :return: un entier indiquant une direction
        """
        if vec == (0, 1):
            return 0  # vers le haut
        elif vec == (1, 0):
            return 1  # vers la gauche
        elif vec == (0, -1):
            return 2  # vers le bas
        else:
            return 3  # vers la droite

    def get_random_dest(self) -> tuple[int, int]:
        """Renvois une destination aléatoire
        :return: une destination aléatoire
        """
        random_x = randint(0, 49)
        random_y = randint(0, 49)
        return random_x, random_y

    def path_2_dir(self, path: list[tuple[int, int]]) -> list[int]:
        """Traduit un chemin composé de positions en directions
        :param path: une liste de positions
        :return: une liste de directions
        """
        if path is not None and type(path) == list:  # si le chemin n'est pas vide et que c'est bien une liste
            directions = []
            if len(path) >= 2:  # s'il y a au moins deux vecteurs dans la liste
                for i in range(len(path) - 1):
                    vec = (path[i][0] - path[i + 1][0], path[i][1] - path[i + 1][1])  # calcule le vecteur de direction
                    for j in range(8):
                        directions.append(self.vec_2_dir(vec))  # ajoute 8 fois la direction dans la liste
                # print(self.owner.name, "- la liste de direction est: ", directions)
                return directions

    def set_destination(self, dest: tuple[int, int]) -> None:
        """Défini la destination à atteindre
        :param dest: une destination
        """
        self.destination = dest

    def do_next_move(self) -> None:
        """Calcule le prochain mouvement de l'entité"""
        if type(self.path) != list:  # si le type du chemin n'est pas une liste
            if not self.algo.get_nb_iterations() >= 30:  # si le nb d'itérations de l'algo A* ne dépasse pas un certain nb
                self.path = self.path_2_dir(self.algo.iteration())  # on continue de chercher une solution
            else:
                self.path = [-1]  # sinon on arrête de chercher une solution
        else:
            next_move = self.path[self.etape]  # défini le prochain mouvement de l'entité

            if next_move == 0:
                self.owner.move_up()  # va en haut
            elif next_move == 1:
                self.owner.move_left()  # va à gauche
            elif next_move == 2:
                self.owner.move_down()  # va en bas
            elif next_move == 3:
                self.owner.move_right()  # va à droite
            else:  # au cas-où
                pass
            self.etape += 1  # incrémente le nb d'étapes

            if self.path is None or self.etape >= len(self.path):  # s'il n'y a pas de chemin de défini ou si la fin du chemin a été atteinte
                self.path = None  # on reset le chemin
                self.etape = 0  # on reset le nb d'étapes
                self.destination = self.get_random_dest()  # on définit une nouvelle destination aléatoire
                self.algo.set_start_pos((int(self.owner.position[0] / 16), int(self.owner.position[1] / 16)))  # on met la position de départ de l'algorithme à la position actuelle de l'entité
                self.algo.set_end_pos(self.destination)  # on définit la position de fin de l'algo à la destination définie plus tôt
                self.algo.reset()  # on remet à 0 l'algo
