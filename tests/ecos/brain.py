from random import randint

from myAstar.astar import Astar


class Brain:
    def __init__(self, owner):
        """Un cerveau pour une créature
        :param owner: le propriétaire du cerveau
        """
        self.owner = owner
        self.etape = 0
        self.grille = self.owner.grille
        self.path = None
        self.destination = self.getRandomDest()
        self.algo = Astar(self.grille, (int(self.owner.position[0] / 16), int(self.owner.position[1] / 16)), self.destination)

    def vec2Dir(self, vec):
        if vec == (0, 1):
            return 0
        elif vec == (1, 0):
            return 1
        elif vec == (0, -1):
            return 2
        else:
            return 3

    def getRandomDest(self):
        randomX = randint(0, 49)
        randomY = randint(0, 49)
        return (randomX, randomY)

    def path2Dir(self, path):
        if path is not None and type(path) == list:
            directions = []
            if len(path) >= 2:
                for i in range(len(path) - 1):
                    vec = (path[i][0] - path[i + 1][0], path[i][1] - path[i + 1][1])
                    for j in range(8):
                        directions.append(self.vec2Dir(vec))
                print(self.owner.name, "- la liste de direction est: ", directions)
                return directions

    def doNextMove(self):
        if type(self.path) != list:
            if not self.algo.get_nb_iterations() >= 30:
                self.path = self.path2Dir(self.algo.iteration())
            else:
                self.path = [-1]
        else:
            nextMove = self.path[self.etape]

            if nextMove == 0:
                self.owner.move_up()
            elif nextMove == 1:
                self.owner.move_left()
            elif nextMove == 2:
                self.owner.move_down()
            elif nextMove == 3:
                self.owner.move_right()
            else:
                pass
            self.etape += 1

            if self.path is None or self.etape >= len(self.path):
                self.path = None
                self.etape = 0
                self.destination = self.getRandomDest()
                self.algo.set_start_pos((int(self.owner.position[0] / 16), int(self.owner.position[1] / 16)))
                self.algo.set_end_pos(self.destination)
                self.algo.reset()
