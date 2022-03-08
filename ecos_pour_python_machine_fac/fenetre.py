import pygame
import sys
from du_code.game import Game
class Fenetre:
    def __init__(self):
        pygame.init()
        #presentation:
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.X = 500
        self.Y = 700
        self.menu_du_jeu = pygame.display.set_mode((500,700))
        pygame.display.set_caption('Menu du Jeu')
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.titre = self.font.render('Ecos',True,self.black)
        self.sous_titre = self.font.render("Simulation d'ecosystème",True,self.black)
        self.textRect = self.titre.get_rect()
        self.textRect2 = self.sous_titre.get_rect()
        self.textRect.center = (self.X//2, 50)
        self.textRect2.center = (self.X//2, 80)

            #boutons:
        self.sfont = pygame.font.Font('freesansbold.ttf',25)

            #mousse
        self.mousse = pygame.mouse.get_pos()
        #print(self.mousse)
    def b_quit(self):
        b_quit = self.sfont.render('Quitter', True, self.white)
        if self.X / 2 <= self.mousse[0] <= self.X / 2 + 140 and self.Y / 2 <= self.mousse[1] <= self.Y / 2 + 40:
            pygame.draw.rect(self.menu_du_jeu, self.black, [self.X / 2 + 100, self.Y / 2 + 300, 140, 40])
        else:
            pygame.draw.rect(self.menu_du_jeu, self.black, [self.X / 2 + 100, self.Y / 2 + 300, 140, 40])
        self.menu_du_jeu.blit(b_quit, (self.X / 2 + 125, self.Y / 2 + 305))

    def b_run(self):
        b_run = self.sfont.render('Lancer', True, self.white)
        if self.X / 2 <= self.mousse[0] <= self.X / 2 + 140 and self.Y / 2 <= self.mousse[1] <= self.Y / 2 + 40:
            pygame.draw.rect(self.menu_du_jeu, self.black, [5, self.Y/2 + 300, 140, 40])
        else:
            pygame.draw.rect(self.menu_du_jeu, self.black, [5, self.Y / 2 + 300, 140, 40])
        self.menu_du_jeu.blit(b_run, (25, self.Y / 2 + 305))


        #boucle while
    def run(self):

        while True:
            self.menu_du_jeu.fill(self.white)
            self.menu_du_jeu.blit(self.titre, self.textRect)
            self.menu_du_jeu.blit(self.sous_titre, self.textRect2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.X/2 <= self.mousse[0] <= self.X/2+140 and self.Y/2 <= self.mousse[1] <= self.Y/2+40:
                        pygame.quit()
            if self.mousse[0] == (355,650) or self.mousse[1] == (480,685):
                pygame.quit()
            if self.mousse[0] == (355,650) or self.mousse[1] == (480,685):
                pygame.quit()
            self.b_quit()
            self.b_run()
            pygame.display.update()

fenetre=Fenetre().run()
