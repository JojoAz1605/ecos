import pygame
from Grille import*


class Window:
    def __init__(self, grille: Grille, width: int, height: int):
        """
        :param grille: une grille
        :param width: la largeur de la fenêtre
        :param height: la hauteur de la fenêtre
        """
        self.grille = grille
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))  # initialise la fenêtre

    # getters
    def getGrid(self):
        return self.grille

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getWindow(self):
        return self.window

    # méthodes
    def afficheGrille(self):
        """Affiche la grille sur la fenêtre
        """
        # TODO potentiellement trouver un autre endroit pour définir ces variables, histoire qu'elle soient pas recalculées à chaque fois
        tailleX = self.width / self.grille.getWidth()  # la largeur d'une case
        tailleY = self.height / self.grille.getHeight()  # la hauteur d'une case
        for x in range(self.grille.getWidth()):
            for y in range(self.grille.getHeight()):
                carreGrille = pygame.Rect(x * tailleX, y * tailleY, tailleX, tailleY)  # la case qui va être affichée
                pygame.draw.rect(self.window, (0, 0, 0), carreGrille, 2)  # dessine la case sur la fenêtre
