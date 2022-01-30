class Grille:
    def __init__(self, height: int, width: int):
        """Une grille, c'est sympa comme truc
        :param height: la hauteur de la grille(le nb d'éléments en y)
        :param width: la largeur de la grille(le nb d'éléments en x)
        """
        self.height = height
        self.width = width
        self.grille = self.initGrille(0)  # initialise une grille avec que des 0 dedans
        self.passable = [0, 2, 3, 4, 5]
        self.window = None

    # getters
    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    # méthodes
    def initGrille(self, defVal):
        """Initialise une grille avec une valeur par défaut donnée
        :param defVal: la valeur par défaut
        :return: la grille
        """
        res = [0] * self.width
        for i in range(self.width):
            res[i] = [defVal] * self.height
        return res

    def afficheGrille(self):
        """Affiche la grille en console
        """
        for ligne in self.grille:
            print(ligne)
        print()  # saute une ligne pour la visibilité

    def setVal(self, pos: tuple, newVal):
        """Change une valeur à une position donnée par une nouvelle
        :param pos: la position de la valeur à changer
        :param newVal: la nouvelle valeur
        """
        self.grille[pos[0]][pos[1]] = newVal
        if self.window is not None:
            self.window.afficheGrille()

    def getVal(self, pos):
        """Retourne la valeur à la position donnée
        :param pos: la position d'une case
        :return: la valeur de la case
        """
        return self.grille[pos[0]][pos[1]]

    def getIsPassable(self, pos):
        val = self.getVal(pos)
        return val in self.passable
