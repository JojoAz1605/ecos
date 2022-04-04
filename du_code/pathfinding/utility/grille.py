class Grille:
    def __init__(self, height: int, width: int) -> None:
        """Une grille, c'est sympa comme truc
        :param height: la hauteur de la grille(le nb d'éléments en y)
        :param width: la largeur de la grille(le nb d'éléments en x)
        """
        self.height = height
        self.width = width
        self.grille = self.init_grille(0)  # initialise une grille avec que des 0 dedans
        self.passable = [0]  # les valeurs dans la grille, qui seront comptées comme traversable par un personnage

    # getters
    def get_height(self) -> int:
        return self.height

    def get_width(self) -> int:
        return self.width

    # méthodes
    def init_grille(self, def_val: int) -> list[int]:
        """Initialise une grille avec une valeur par défaut donnée
        :param def_val: la valeur par défaut
        :return: la grille
        """
        res = [0] * self.width
        for i in range(self.width):
            res[i] = [def_val] * self.height
        return res

    def affiche_grille(self) -> None:
        """Affiche la grille en console
        """
        for ligne in self.grille:
            print(ligne)
        print()  # saute une ligne pour la visibilité

    def set_val(self, pos: tuple[int, int], new_val: int) -> None:
        """Change une valeur à une position donnée par une nouvelle
        :param pos: la position de la valeur à changer
        :param new_val: la nouvelle valeur
        """
        self.grille[pos[0]][pos[1]] = new_val

    def get_val(self, pos: tuple[int, int]) -> int:
        """Retourne la valeur à la position donnée
        :param pos: la position d'une case
        :return: la valeur de la case
        """
        try:
            return self.grille[pos[0]][pos[1]]
        except IndexError:
            pass

    def get_is_passable(self, pos: tuple[int, int]) -> bool:
        """Retourne si la valeur à une position donnée est traversable
        :return: oui ou non
        """
        return self.get_val(pos) in self.passable
