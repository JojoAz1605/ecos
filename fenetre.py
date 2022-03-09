import pygame
import sys
from du_code.game import Game
class Fenetre:
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
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
        self.rect_quit=self.b_quit()
        self.rect_run=self.b_run()

            #boutons:
        self.sfont = pygame.font.Font('freesansbold.ttf',25)

            #mousse
        self.mousse = pygame.mouse.get_pos()
        #print(self.mousse)
    def b_quit(self):
        rect_quit = self.menu_du_jeu, self.black, [self.X / 2 + 100, self.Y / 2 + 300, 140, 40]
        bquit = self.font.render('Quitter', True, self.white)
        self.menu_du_jeu.blit(bquit, (self.X / 2 + 125, self.Y / 2 + 305))
        return bquit.get_rect()

    def b_run(self):
        rect_run = self.menu_du_jeu, self.black, [5, self.Y / 2 + 300, 140, 40]
        brun = self.font.render('Lancer', True, self.white)
        self.menu_du_jeu.blit(brun, (25, self.Y / 2 + 305))
        return brun.get_rect()


        #boucle while
    def run(self):
        allSprites=pygame.sprite.Group(self.rect_quit,self.rect_run)
        while True:
            if pygame.sprite.spritecollide(pygame.mouse.get_pos(),allSprites,True):
                print('Colision')
            self.menu_du_jeu.fill(self.white)
            self.menu_du_jeu.blit(self.titre, self.textRect)
            self.menu_du_jeu.blit(self.sous_titre, self.textRect2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousse
                    clicked_sprites = [s for s in sprites if s.rect.collidepoint(self.mousse)]
            self.b_quit()
            self.b_run()
            pygame.display.update()

fenetre=Fenetre().run()
