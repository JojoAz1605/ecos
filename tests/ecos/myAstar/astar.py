from .graph import Graph
from .node import Node


class Astar:
    def __init__(self, grid, startPos, endPos):
        self.graph = Graph(grid, startPos, endPos)
        self.open = [self.graph.getStartNode()]
        self.close = []
        self.nbIterations = 0

    def reconstruct(self):
        path = [self.close[-1]]
        parent = path[-1].getParent()
        while parent != self.graph.getStartNode():
            parent = path[-1].getParent()
            path.append(parent)
        self.reset()
        path.reverse()
        return path

    def reset(self):
        self.open = [self.graph.getStartNode()]
        self.close = []
        self.nbIterations = 0

    def afficheListe(self, liste):
        for elem in liste:
            print(elem, end=',')
        print()

    def isInList(self, oneNode, liste):
        for node in liste:
            if node == oneNode:
                return True
        return False

    def __updateIfAlreadyInOpenAndWithBetterScore(self, studiedNode, successor):
        if successor in self.open and successor.getScore() < self.open.index(successor):
            self.open.remove(successor)
            self.open.append(successor)
        else:
            self.open.append(Node(
                self.graph,
                successor.pos,
                successor.getIsPassable,
                studiedNode
            ))

    def convertToPos(self):
        res = []
        for node in self.reconstruct():
            self.graph.grid.setVal(node.getPos(), 2)
            res.append(node.pos)
        return res

    def __getBestNodeInOpen(self):
        best = self.open[0]
        for node in self.open:
            if node.getScore() < best.getScore():
                best = node
        return best

    def getNbIterations(self):
        return self.nbIterations

    def setEndPos(self, pos):
        self.graph.setEndNode(Node(self.graph, pos, self.graph.grid.getVal(pos), None))

    def setStartPos(self, pos):
        self.graph.setStartNode(Node(self.graph, pos, self.graph.grid.getVal(pos), None))

    def iteration(self):
        self.nbIterations += 1
        if len(self.close) != 0:
            node = self.close[-1]
            # print(len(self.open), len(self.close), node.getPos(), node.calculateManhattanDist(), self.graph.endNode.pos)
        else:
            node = self.open[0]
        successors = node.getSuccessors()
        for successor in successors:
            if self.isInList(successor, self.close):
                continue
            self.__updateIfAlreadyInOpenAndWithBetterScore(node, successor)
        if len(self.open) == 0:
            print("pas de solution")
            return None
        else:
            bestNodeInOpen = self.__getBestNodeInOpen()
            self.open.remove(bestNodeInOpen)
            self.close.append(bestNodeInOpen)
            if self.close[-1] == self.graph.getEndNode():
                print("Solution pour aller de", self.graph.getStartNode().pos, "jusqu'à",
                      self.graph.getEndNode().pos)
                self.afficheListe(self.close)
                return self.convertToPos()
        return False
