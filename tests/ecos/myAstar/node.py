class Node:
    def __init__(self, graph, pos: tuple[int, int], parent) -> None:
        """Un noeud d'un graph
        :param graph: le graph
        :param pos: une position
        :param parent: le parent du noeud ou None s'il n'en a pas
        """
        self.graph = graph
        self.pos = pos
        self.is_passable = self.graph.grid.get_is_passable(self.pos)
        if parent is None:  # si le nœud n'a pas de parent
            self.parent = self  # il est son propre parent
        else:
            self.parent = parent  # sinon prend la valeur donnée
        self.f_score = 0  # score du noeud
        self.g_score = 0  # distance de manhattan du noeud par rapport à son parent
        self.h_score = 0  # distance de manhattan du noeud par rapport à la destination

    def __eq__(self, other) -> bool:
        """Si le noeud possède la même position qu'un autre noeud, alors ce sont les mêmes"""
        return self.pos == other.pos

    def __str__(self) -> str:
        """Pour l'affichage console"""
        return str(self.pos)

    def __calculate_g(self) -> None:
        """Calcule le score G"""
        node = self.parent
        self.g_score = abs(node.pos[0] - self.pos[0]) + abs(node.pos[1] - self.pos[1])

    def __calculate_h(self) -> None:
        """Calcule le score H"""
        node = self.graph.get_end_node()
        self.h_score = abs(self.pos[0] - node.pos[0]) + abs(self.pos[1] - node.pos[1])

    def get_pos(self) -> tuple[int, int]:
        return self.pos

    def get_parent(self):
        return self.parent

    def get_score(self) -> int:
        """Calcule le score et le retourne
        :return: le score de la node
        """
        self.__calculate_g()
        self.__calculate_h()
        self.f_score = self.g_score + self.h_score
        return self.f_score

    def get_is_passable(self) -> bool:
        return self.is_passable

    def set_parent(self, parent) -> None:
        self.parent = parent

    def __get_neigbours_nodes(self) -> list:
        """Retourne les nodes adjacentes
        :return: les nodes adjacentes
        """
        res = []

        node_x = self.pos[0]
        node_y = self.pos[1]
        if node_x + 1 < self.graph.grid.width:
            res.append(Node(self.graph, (node_x + 1, node_y), self))
        if node_x - 1 > 0:
            res.append(Node(self.graph, (node_x - 1, node_y), self))
        if node_y + 1 < self.graph.grid.height:
            res.append(Node(self.graph, (node_x, node_y + 1), self))
        if node_y - 1 > 0:
            res.append(Node(self.graph, (node_x, node_y - 1), self))

        return res

    def get_successors(self) -> list:
        """Donne les successeurs de la node
        :return: les successeurs de la node
        """
        res = []
        neighbors = self.__get_neigbours_nodes()  # prend ses voisins
        for neighbor in neighbors:  # pour tous les voisins
            if neighbor.get_is_passable():  # si le voisin est traversable
                res.append(neighbor)  # l'ajoute au résultat
        return res

