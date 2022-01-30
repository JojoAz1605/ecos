from .graph import Graph
from .grille import Grille
from .node import Node


class Astar:
    def __init__(self, grid: Grille, startPos: tuple, endPos: tuple):
        """L'algorithme A*, filez lui une grille, un début et une fin, il trouvera le chemin tout seul ;)
        :param grid: une grille pour que l'algorithme puisse se retrouver
        :param startPos: la position de départ
        :param endPos: la position d'arrivée
        """
        self.graph = Graph(grid, startPos, endPos)
        self.open = [self.graph.getStartNode()]  # la liste ouverte, stockant les nœuds qui restent à explorer
        self.close = []  # la liste fermée, stockant les nœuds les plus prometteurs
        self.nbIterations = 0  # le nombre actuel d'itération de l'algorithme

    def __reconstruct(self):
        """Sert pour reconstruire tout le chemin qu'a trouvé l'algo
        :return: un chemin sous forme de node allant de la position de départ à la position de fin
        """
        path = [self.close[-1]]  # prend le dernier nœud de la liste fermée
        parent = path[-1].getParent()  # prend son parent
        while parent != self.graph.getStartNode():  # tant que le nœud parent n'est pas le nœud de départ
            parent = path[-1].getParent()  # prend le parent du dernier noeud ajouté à la liste
            path.append(parent)  # et l'ajoute à la liste
        self.reset()  # reset l'algorithme
        path.reverse()  # retourne la liste(sinon on commencerait de la fin)
        return path

    def reset(self):
        """Remet à 0 l'algorithme"""
        self.open = [self.graph.getStartNode()]
        self.close = []
        self.nbIterations = 0

    def __isInList(self, oneNode: Node, liste: list):
        """Voit si une node est dans la liste donnée
        :param oneNode: une node
        :param liste: une autre node
        :return: oui ou non
        """
        for node in liste:  # parcours des nodes
            if node == oneNode:  # si une node correspond
                return True  # alors oui
        return False  # sinon non

    def __updateIfAlreadyInOpenAndWithBetterScore(self, studiedNode: Node, successor: Node):
        """Voit si une node est déjà dans la liste ouverte, et avec un meilleur score
        si oui: met à jour son parent
        sinon: l'ajoute à la liste
        :param studiedNode: le noeud qui est étudié par la boucle principale
        :param successor: un noeud qui succède au noeud étudié
        """
        if successor in self.open and successor.getScore() < self.open.index(successor):  # si le successeur est dans la liste et à un score inférieur
            self.open.remove(successor)  # retire celui qui a un score inférieur
            self.open.append(successor)  # et ajoute celui qui a un meilleur score à la place
        else:  # sinon l'ajoute à la liste
            self.open.append(Node(
                self.graph,
                successor.pos,
                successor.getIsPassable,
                studiedNode
            ))

    def __convertToPos(self):
        """Convertit les nodes du résultat en positions exploitables par un cerveau de créature
        :return: des positions
        """
        res = []
        for node in self.__reconstruct():  # pour tous les noeuds dans le chemin reconstruit
            res.append(node.pos)  # ajoute la position de la node à la liste
        return res

    def __getBestNodeInOpen(self):
        """Cherche la meilleure node dans la liste ouverte et la retourne
        :return: la meilleure node dans la liste ouverte
        """
        best = self.open[0]  # on prend la première node
        for node in self.open:
            if node.getScore() < best.getScore():  # si une node est meilleure
                best = node  # on remplace la meilleure par celle-ci
        return best

    def getNbIterations(self):
        return self.nbIterations

    def setEndPos(self, pos: tuple):
        self.graph.setEndNode(Node(self.graph, pos, self.graph.grid.getVal(pos), None))

    def setStartPos(self, pos: tuple):
        self.graph.setStartNode(Node(self.graph, pos, self.graph.grid.getVal(pos), None))

    def iteration(self):
        """Une itération de l'algorithme
        :return: False si toujours pas fini ou une liste de positions si fini et None si aucun résultat
        """
        self.nbIterations += 1
        if len(self.close) != 0:  # si la liste fermée n'est pas vide
            node = self.close[-1]  # le noeud étudié est le dernier de la liste fermée
        else:
            node = self.open[0]  # sinon c'est le premier de la liste ouverte
        successors = node.getSuccessors()  # prend tous les successeurs de la node étudiée
        for successor in successors:
            if self.__isInList(successor, self.close):  # si le successeur est dans la liste fermée
                continue  # on l'ignore et on passe au successeur suivant
            self.__updateIfAlreadyInOpenAndWithBetterScore(node, successor)  # voit si le successeur est dans la liste ouverte
        if len(self.open) == 0:  # si la liste ouverte se vide entièrement
            print("pas de solution")
            return None  # aucune solution, None est retourné
        else:
            bestNodeInOpen = self.__getBestNodeInOpen()  # prend la meilleure node dans la liste ouverte
            self.open.remove(bestNodeInOpen)  # la retire de la liste ouverte
            self.close.append(bestNodeInOpen)  # et l'ajoute à la liste fermée
            if self.close[-1] == self.graph.getEndNode():  # si la dernière node de la liste fermée est la destination
                return self.__convertToPos()  # retourne un résultat(en le convertissant dans un meilleur format au passage)
        return False  # si l'itération se termine sans problème, retourne False
