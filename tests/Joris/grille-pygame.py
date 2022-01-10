# création et affichage de grille en console

class Grille:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grille = self.initGrille(0)

    def initGrille(self, defVal):
        res = [0] * self.width
        for i in range(self.width):
            res[i] = [defVal] * self.height
        return res

    def afficheGrille(self):
        for ligne in self.grille:
            print(ligne)
        print()

    def changerVal(self, pos, newVal):
        self.grille[pos[0]][pos[1]] = newVal


grille = Grille(5, 5)
grille.afficheGrille()
grille.changerVal((3, 3), 3)
grille.afficheGrille()

# affichage via pygame

