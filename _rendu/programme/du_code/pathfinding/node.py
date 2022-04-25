class Node:
    def __init__(self, algo, pos: tuple[int, int], parent) -> None:
        """Un noeud d'un algo
        :param algo: l'algo
        :param pos: une position
        :param parent: le parent du noeud ou None s'il n'en a pas
        """
        self.algo = algo
        self.pos = pos
        self.is_passable = self.algo.grid.get_is_passable(self.pos)
        if parent is None:  # si le nœud n'a pas de parent
            self.parent = self  # il est son propre parent
        else:
            self.parent = parent  # sinon prend la valeur donnée

    def __eq__(self, other) -> bool:
        """Si le noeud possède la même position qu'un autre noeud, alors ce sont les mêmes"""
        return self.pos == other.pos

    def __str__(self) -> str:
        """Pour l'affichage console"""
        return str(self.pos)

    def get_parent(self):
        return self.parent

    def get_score(self) -> int:
        """Calcule le score et le retourne
        :return: le score de la node_h
        """
        node_g = self.parent
        node_h = self.algo.get_end_node()

        return (abs(node_g.pos[0] - self.pos[0]) + abs(node_g.pos[1] - self.pos[1])) + (abs(self.pos[0] - node_h.pos[0]) + abs(self.pos[1] - node_h.pos[1]))

    def get_is_passable(self) -> bool:
        return self.is_passable

    def set_parent(self, parent) -> None:
        self.parent = parent

    def get_successors(self) -> list:
        """Donne les successeurs de la node
        :return: les successeurs de la node
        """
        res = []

        if self.pos[0] + 1 < self.algo.grid.width and self.algo.grid.get_is_passable((self.pos[0] + 1, self.pos[1])):
            res.append(Node(self.algo, (self.pos[0] + 1, self.pos[1]), self))
        if self.pos[0] - 1 > 0 and self.algo.grid.get_is_passable((self.pos[0] - 1, self.pos[1])):
            res.append(Node(self.algo, (self.pos[0] - 1, self.pos[1]), self))
        if self.pos[1] + 1 < self.algo.grid.height and self.algo.grid.get_is_passable((self.pos[0], self.pos[1] + 1)):
            res.append(Node(self.algo, (self.pos[0], self.pos[1] + 1), self))
        if self.pos[1] - 1 > 0 and self.algo.grid.get_is_passable((self.pos[0], self.pos[1] - 1)):
            res.append(Node(self.algo, (self.pos[0], self.pos[1] - 1), self))

        return res
