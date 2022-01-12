import pygame
from Grille import*
from lesCouleurs import*

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
        self.tailleCases = (self.width / self.grille.getWidth(), self.height / self.grille.getHeight())  # la taille des cases sur la grille

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
        for x in range(self.grille.getWidth()):
            for y in range(self.grille.getHeight()):
                caseVal = self.grille.getVal((x, y))
                color = colors[dicoStates[caseVal]]
                carreGrille = pygame.Rect(x * self.tailleCases[0], y * self.tailleCases[1], self.tailleCases[0], self.tailleCases[1])  # la case qui va être affichée
                pygame.draw.rect(self.window, color, carreGrille)  # dessine la case sur la fenêtre
