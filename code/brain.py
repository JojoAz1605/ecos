from random import randint
from code.pathfinding.astar import Astar


class Brain:
    def __init__(self, owner):
        """Un cerveau pour une créature
        :param owner: le propriétaire du cerveau
        """
        self.owner = owner
        self.etape = 0
        self.grille = self.owner.grille
        self.path = None
        self.destination = self.get_random_dest()
        self.algo = Astar(self.grille, (int(self.owner.position[0] / 16), int(self.owner.position[1] / 16)), self.destination)

    def vec_2_dir(self, vec):
        if vec == (0, 1):
            return 0
        elif vec == (1, 0):
            return 1
        elif vec == (0, -1):
            return 2
        else:
            return 3

    def get_random_dest(self):
        random_x = randint(0, 49)
        random_y = randint(0, 49)
        return (random_x, random_y)

    def path_2_dir(self, path):
        if path is not None and type(path) == list:
            directions = []
            if len(path) >= 2:
                for i in range(len(path) - 1):
                    vec = (path[i][0] - path[i + 1][0], path[i][1] - path[i + 1][1])
                    for j in range(8):
                        directions.append(self.vec_2_dir(vec))
                # print(self.owner.name, "- la liste de direction est: ", directions)
                return directions

    def go_to(self, dest: tuple[int, int]):
        self.destination = dest

    def do_next_move(self):
        if type(self.path) != list:
            if not self.algo.get_nb_iterations() >= 30:
                self.path = self.path_2_dir(self.algo.iteration())
            else:
                self.path = [-1]
        else:
            next_move = self.path[self.etape]

            if next_move == 0:
                self.owner.move_up()
            elif next_move == 1:
                self.owner.move_left()
            elif next_move == 2:
                self.owner.move_down()
            elif next_move == 3:
                self.owner.move_right()
            else:
                pass
            self.etape += 1

            if self.path is None or self.etape >= len(self.path):
                self.path = None
                self.etape = 0
                self.destination = self.get_random_dest()
                self.algo.set_start_pos((int(self.owner.position[0] / 16), int(self.owner.position[1] / 16)))
                self.algo.set_end_pos(self.destination)
                self.algo.reset()
