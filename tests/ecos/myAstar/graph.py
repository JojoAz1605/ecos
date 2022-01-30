from .node import Node
from .grille import Grille


class Graph:
    def __init__(self, grid: Grille, startPos: tuple, endPos: tuple):
        """Pour représenter la grille et ses nodes, plutôt que d'avoir une grille de node
        :param grid: une grille
        :param startPos: une position de départ
        :param endPos: une position de fin
        """
        self.grid = grid
        self.startNode = Node(self, startPos, self.grid.getVal(startPos), None)
        self.endNode = Node(self, endPos, self.grid.getVal(endPos), None)

    def setStartNode(self, node: Node):
        self.startNode = node

    def setEndNode(self, node: Node):
        self.endNode = node

    def getStartNode(self):
        return self.startNode

    def getEndNode(self):
        return self.endNode
