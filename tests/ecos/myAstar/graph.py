from .node import Node
from .grille import Grille


class Graph:
    def __init__(self, grid: Grille, start_pos: tuple, end_pos: tuple) -> None:
        """Pour représenter la grille et ses nodes, plutôt que d'avoir une grille de node
        :param grid: une grille
        :param start_pos: une position de départ
        :param end_pos: une position de fin
        """
        self.grid = grid
        self.start_node = Node(self, start_pos, self.grid.get_val(start_pos), None)
        self.end_node = Node(self, end_pos, self.grid.get_val(end_pos), None)

    def set_start_node(self, node: Node) -> None:
        self.start_node = node

    def set_end_node(self, node: Node) -> None:
        self.end_node = node

    def get_start_node(self) -> Node:
        return self.start_node

    def get_end_node(self) -> Node:
        return self.end_node
