class Node:
    def __init__(self, graph, pos, isPassable, parent):
        self.graph = graph
        self.pos = pos
        self.isPassable = isPassable
        if parent is None:
            self.parent = self
        else:
            self.parent = parent
        self.fScore = 0
        self.gScore = 0
        self.hScore = 0

    def __eq__(self, other):
        return self.pos == other.pos

    def __str__(self):
        return str(self.pos)

    def __calculateG(self):
        node = self.parent
        self.gScore = abs(node.pos[0] - self.pos[0]) + abs(node.pos[1] - self.pos[1])

    def __calculateH(self):
        node = self.graph.getEndNode()
        self.gScore = abs(self.pos[0] - node.pos[0]) + abs(self.pos[1] - node.pos[1])

    def getPos(self):
        return self.pos

    def calculateManhattanDist(self):
        node = self.graph.getEndNode()
        return abs(self.pos[0] - node.pos[0]) + abs(self.pos[1] - node.pos[1])

    def getParent(self):
        return self.parent

    def getScore(self):
        self.__calculateG()
        self.__calculateH()
        self.fScore = self.gScore + self.hScore
        return self.fScore

    def getIsPassable(self):
        return self.isPassable

    def setParent(self, parent):
        self.parent = parent

    def __getNeigboursNodes(self):
        res = []

        nodeX = self.pos[0]
        nodeY = self.pos[1]
        if nodeX + 1 < self.graph.grid.width:
            res.append(Node(self.graph,
                            (nodeX + 1, nodeY),
                            self.graph.grid.getIsPassable((nodeX + 1, nodeY)),
                            self
                            ))
        if nodeX - 1 > 0:
            res.append(Node(self.graph,
                            (nodeX - 1, nodeY),
                            self.graph.grid.getIsPassable((nodeX - 1, nodeY)),
                            self
                            ))
        if nodeY + 1 < self.graph.grid.height:
            res.append(Node(self.graph,
                            (nodeX, nodeY + 1),
                            self.graph.grid.getIsPassable((nodeX, nodeY + 1)),
                            self
                            ))
        if nodeY - 1 > 0:
            res.append(Node(self.graph,
                            (nodeX, nodeY - 1),
                            self.graph.grid.getIsPassable((nodeX, nodeY - 1)),
                            self
                            ))

        return res

    def getSuccessors(self):
        res = []
        neighbors = self.__getNeigboursNodes()
        for neighbor in neighbors:
            if neighbor.getIsPassable():
                res.append(neighbor)
        return res

