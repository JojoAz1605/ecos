import pygame
import pygame.sprite
import pygame.font
import sys
from du_code.game import Game
#presentation:
pygame.init()
white = (255,255,255)
black = (0,0,0)
X = 500
Y = 700
menu_du_jeu = pygame.display.set_mode((500,700))
pygame.display.set_caption('Menu du Jeu')
fontE = pygame.font.SysFont('arial',32)
titre = fontE.render('Ecos',True,black)
sous_titre = fontE.render("Simulation d'ecosystème",True,black)
textRect = titre.get_rect()
textRect2 = sous_titre.get_rect()
textRect.center = (X//2, 50)
textRect2.center = (X//2, 80)
sfont = pygame.font.SysFont('arial',25)
#mouse
mousse = pygame.mouse.get_pos()
#print(mousse)
class Rect_quit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = menu_du_jeu, black, [X / 2 + 100, Y / 2 + 300, 140, 40]
    def b_quit(self):
        global white, black, X, Y, menu_du_jeu, fontE
        self.bquit = fontE.render('Quitter', True, white)
        menu_du_jeu.blit(bquit, (X / 2 + 125, Y / 2 + 305))
        return bquit.get_rect()

class Rect_run(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    def b_run(self):
        global white, black, Y, menu_du_jeu, fontE
        self.rect_run = menu_du_jeu, black, [5, Y / 2 + 300, 140, 40]
        self.brun = fontE.render('Lancer', True, white)
        menu_du_jeu.blit(brun, (25, Y / 2 + 305))
        return brun.get_rect()

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        global mousse
        pygame.sprite.Sprite.__init__(self)
        self.rect=pygame.Rect(mousse,(4,4))
    def update(self):
        rect.center=pygame.mouse.get_pos()

class Fenetre:
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        #boucle while
    def run(self):
        global white, menu_du_jeu, titre, sous_titre, textRect, textRect2, mousse
        souris=Mouse()
        allSprites=pygame.sprite.Group()
        allSprites.add(Rect_quit())
        allSprites.add(Rect_run())
        
        while True:
            if pygame.sprite.spritecollide(souris.rect,allSprites,True):
                print ("collision")
            menu_du_jeu.fill(white)
            menu_du_jeu.blit(titre, textRect)
            menu_du_jeu.blit(sous_titre,textRect2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEMOTION :
                   for s in allSprites : 
                        if pygame.sprite.collide_rect(s,souris):
                            pygame.quit()
            self.b_quit()
            self.b_run()
            pygame.display.update()

fenetre=Fenetre().run()
