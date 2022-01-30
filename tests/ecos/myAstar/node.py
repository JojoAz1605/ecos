class Node:
    def __init__(self, graph, pos: tuple, isPassable: bool, parent):
        """Un noeud d'un graph
        :param graph: le graph
        :param pos: une position
        :param isPassable: si le noeud est traversable
        :param parent: le parent du noeud
        """
        self.graph = graph
        self.pos = pos
        self.isPassable = isPassable
        if parent is None:  # si le noeud n'a pas de parent
            self.parent = self  # il est son propre parent
        else:
            self.parent = parent  # sinon prend la valeur donnée
        self.fScore = 0  # score du noeud
        self.gScore = 0  # distance de manhattan du noeud par rapport à son parent
        self.hScore = 0  # distance de manhattan du noeud par rapport à la destination

    def __eq__(self, other):
        """Si le noeud possède la même position qu'un autre noeud, alors ce sont les mêmes"""
        return self.pos == other.pos

    def __str__(self):
        """Pour l'affichage console"""
        return str(self.pos)

    def __calculateG(self):
        """Calcule le score G"""
        node = self.parent
        self.gScore = abs(node.pos[0] - self.pos[0]) + abs(node.pos[1] - self.pos[1])

    def __calculateH(self):
        """Calcule le score H"""
        node = self.graph.getEndNode()
        self.hScore = abs(self.pos[0] - node.pos[0]) + abs(self.pos[1] - node.pos[1])

    def getPos(self):
        return self.pos

    def getParent(self):
        return self.parent

    def getScore(self):
        """Calcule le score et le retourne
        :return:
        """
        self.__calculateG()
        self.__calculateH()
        self.fScore = self.gScore + self.hScore
        return self.fScore

    def getIsPassable(self):
        return self.isPassable

    def setParent(self, parent):
        self.parent = parent

    def __getNeigboursNodes(self):
        """Retourne les nodes adjacentes
        :return: les nodes adjacentes
        """
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
        """Donne les successeurs de la node
        :return: les successeur de la node
        """
        res = []
        neighbors = self.__getNeigboursNodes()  # prend ses voisins
        for neighbor in neighbors:  # pour tous les voisins
            if neighbor.getIsPassable():  # si le voisin est traversable
                res.append(neighbor)  # l'ajoute au résultat
        return res

