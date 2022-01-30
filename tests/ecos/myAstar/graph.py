from .node import Node


class Graph:
    def __init__(self, grid, startPos, endPos):
        self.grid = grid
        self.startNode = Node(self, startPos, self.grid.getVal(startPos), None)
        self.endNode = Node(self, endPos, self.grid.getVal(endPos), None)

    def setStartNode(self, node):
        self.startNode = node

    def setEndNode(self, node):
        self.endNode = node

    def getStartNode(self):
        return self.startNode

    def getEndNode(self):
        return self.endNode
