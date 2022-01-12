import sys

import pygame.font

from Window import *
from random import randint
from lesCouleurs import*

# affichage via pygame

pygame.init()  # initialise pygame(quoi que ça veuille dire)

WIN_HEIGHT = 700  # hauteur de la fenêtre
WIN_WIDTH = 700  # largeur de la fenêtre

grille = Grille(100, 100)  # initialisation d'une grille

fenetre = Window(grille, WIN_WIDTH, WIN_HEIGHT)  # initialise une fenêtre
fenetre.getWindow().fill((255, 255, 255))  # rempli la fenêtre de noir

maPolice = pygame.font.SysFont("monospace", 80)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pour gérer la sortie de la fenêtre avec la petite croix en haut à droite
            sys.exit()

    for i in range(randint(0, 100)):
        fenetre.grille.changerVal((randint(0, fenetre.getGrid().getWidth() - 1), randint(0, fenetre.getGrid().getHeight() - 1)), randint(0, 4))

    labelColor = (randint(0, 255), randint(0, 255), randint(0, 255))

    fenetre.afficheGrille()  # affiche la grille sur la fenêtre
    label = maPolice.render("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", True, labelColor)
    fenetre.window.blit(label, (randint(0, fenetre.getWidth() - 1), randint(0, fenetre.getHeight() - 1)))

    pygame.display.flip()  # alors
