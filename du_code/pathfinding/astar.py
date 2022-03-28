from du_code.pathfinding.utility.grille import Grille
from .node import Node


class Astar:
    def __init__(self, grid: Grille, start_pos: tuple[int, int], end_pos: tuple[int, int], brain) -> None:
        """L'algorithme A*, filez lui une grille, un début et une fin, il trouvera le chemin tout seul ;)
        :param grid: une grille pour que l'algorithme puisse se retrouver
        :param start_pos: la position de départ
        :param end_pos: la position d'arrivée
        """
        self.grid = grid
        self.start_node = Node(self, start_pos, None)
        self.end_node = Node(self, end_pos, None)
        self.brain = brain
        self.open = [self.start_node]  # la liste ouverte, stockant les nœuds qui restent à explorer
        self.close = []  # la liste fermée, stockant les nœuds les plus prometteurs
        self.nb_iterations = 0  # le nombre actuel d'itération de l'algorithme

    def __reconstruct(self) -> list[Node]:
        """Sert pour reconstruire tout le chemin qu'a trouvé l'algo
        :return: un chemin sous forme de node allant de la position de départ à la position de fin
        """
        path = [self.close[-1]]  # prend le dernier nœud de la liste fermée
        parent = path[-1].get_parent()  # prend son parent
        while parent != self.get_start_node():  # tant que le nœud parent n'est pas le nœud de départ
            parent = path[-1].get_parent()  # prend le parent du dernier noeud ajouté à la liste
            path.append(parent)  # et l'ajoute à la liste
        self.reset()  # reset l'algorithme
        path.reverse()  # retourne la liste(sinon on commencerait de la fin)
        return path

    def reset(self) -> None:
        """Remet à 0 l'algorithme"""
        self.open = [self.get_start_node()]
        self.close = []
        self.nb_iterations = 0

    def __is_in_list(self, one_node: Node, liste: list[Node]) -> bool:
        """Voit si une node est dans la liste donnée
        :param one_node: une node
        :param liste: une autre node
        :return: oui ou non
        """
        for node in liste:  # parcours des nodes
            if node == one_node:  # si une node correspond
                return True  # alors oui
        return False  # sinon non

    def __update_if_already_in_open_and_with_better_score(self, studied_node: Node, successor: Node) -> None:
        """Voit si une node est déjà dans la liste ouverte, et avec un meilleur score
        si oui: met à jour son parent
        sinon: l'ajoute à la liste
        :param studied_node: le noeud qui est étudié par la boucle principale
        :param successor: un noeud qui succède au noeud étudié
        """
        if successor in self.open and successor.get_score() < self.open.index(successor):  # si le successeur est dans la liste et à un score inférieur
            self.open.remove(successor)  # retire celui qui a un score inférieur
            self.open.append(successor)  # et ajoute celui qui a un meilleur score à la place
        else:  # sinon l'ajoute à la liste
            self.open.append(Node(self, successor.pos, studied_node))

    def __convert_to_pos(self) -> list[tuple[int, int]]:
        """Convertit les nodes du résultat en positions exploitables par un cerveau de créature
        :return: des positions
        """
        res = []
        for node in self.__reconstruct():  # pour tous les noeuds dans le chemin reconstruit
            res.append(node.pos)  # ajoute la position de la node à la liste
        return res

    def __get_best_node_in_open(self) -> Node:
        """Cherche la meilleure node dans la liste ouverte et la retourne
        :return: la meilleure node dans la liste ouverte
        """
        best = self.open[0]  # on prend la première node
        for node in self.open:
            if node.get_score() < best.get_score():  # si une node est meilleure
                best = node  # on remplace la meilleure par celle-ci
        return best

    def get_nb_iterations(self) -> int:
        return self.nb_iterations

    def get_start_node(self) -> Node:
        return self.start_node

    def get_end_node(self) -> Node:
        return self.end_node

    def set_start_node(self, node: Node) -> None:
        self.start_node = node

    def set_end_node(self, node: Node) -> None:
        self.end_node = node

    def set_start_pos(self, pos) -> None:
        self.set_start_node(Node(self, pos, None))

    def set_end_pos(self, pos) -> None:
        self.set_end_node(Node(self, pos, None))

    def iteration(self) -> None or bool:
        """Une itération de l'algorithme
        :return: False si toujours pas fini ou une liste de positions si fini et None si aucun résultat
        """
        self.nb_iterations += 1
        if len(self.close) != 0:  # si la liste fermée n'est pas vide
            node = self.close[-1]  # le noeud étudié est le dernier de la liste fermée
        else:
            node = self.open[0]  # sinon c'est le premier de la liste ouverte
        successors = node.get_successors()  # prend tous les successeurs de la node étudiée
        for successor in successors:
            if self.__is_in_list(successor, self.close):  # si le successeur est dans la liste fermée
                continue  # on l'ignore et on passe au successeur suivant
            self.__update_if_already_in_open_and_with_better_score(node, successor)  # voit si le successeur est dans la liste ouverte
        if len(self.open) == 0:  # si la liste ouverte se vide entièrement
            print(f"\tAH! On dirait que {self.brain.owner.name} est sorti de la matrice :o")
            self.brain.owner.kill()
            return None  # aucune solution, None est retourné
        else:
            best_node_in_open = self.__get_best_node_in_open()  # prend la meilleure node dans la liste ouverte
            self.open.remove(best_node_in_open)  # la retire de la liste ouverte
            self.close.append(best_node_in_open)  # et l'ajoute à la liste fermée
            if self.close[-1] == self.get_end_node():  # si la dernière node de la liste fermée est la destination
                return self.__convert_to_pos()  # retourne un résultat(en le convertissant dans un meilleur format au passage)
        return False  # si l'itération se termine sans problème, retourne False
