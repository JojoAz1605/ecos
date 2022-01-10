import sys
from Window import *

# création et affichage de grille en console
grille = Grille(5, 5)
grille.afficheGrille()
grille.changerVal((3, 3), 3)
grille.afficheGrille()

# affichage via pygame

pygame.init()  # initialise pygame(quoi que ça veuille dire)

WIN_HEIGHT = 500  # hauteur de la fenêtre
WIN_WIDTH = 500  # largeur de la fenêtre

grille = Grille(5, 5)  # initialisation d'une grille

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pour gérer la sortie de la fenêtre avec la petite croix en haut à droite
            sys.exit()

    fenetre = Window(grille, WIN_WIDTH, WIN_HEIGHT)  # initialise une fenêtre
    fenetre.getWindow().fill((255, 255, 255))  # rempli la fenêtre de noir

    # TODO les changements sur la grille se répercutent sur le dessin
    fenetre.afficheGrille()  # affiche la grille sur la fenêtre

    pygame.display.flip()  # alors
