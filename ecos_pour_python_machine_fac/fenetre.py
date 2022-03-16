import pygame
from du_code.game import Game
#presentation et declaration:
pygame.init()
game = Game()
para = Para()
white = (255,255,255)
black = (0,0,0)
X = 500
Y = 700
menu_du_jeu = pygame.display.set_mode((500,700))
pygame.display.set_caption('Menu du Jeu')


#creation des titres et sous:
fontE = pygame.font.SysFont('arial',32)
titre = fontE.render('Ecos',True,black)
sous_titre = fontE.render("Simulation d'ecosystème",True,black)
textRect = titre.get_rect()
textRect2 = sous_titre.get_rect()
textRect.center = (X//2, 50)
textRect2.center = (X//2, 80)
#creation d'une police pour les boutons:
sfont = pygame.font.SysFont('arial',25)
#creation de la souris:
mousse = pygame.mouse.get_pos()

#definition du rectangle pour quitter la menu:
class Rect_quit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((140,40))
        self.image.fill(black)
        self.rect=self.image.get_rect()
        self.rect.center=(X / 2 + 170, Y / 2 + 300)
        
    '''def b_quit(self):
        global white, black, X, Y, menu_du_jeu, fontE
        self.bquit = fontE.render('Quitter', True, white)
        menu_du_jeu.blit(bquit, (X / 2 + 125, Y / 2 + 305))
        return bquit.get_rect()'''
    

#definition du rectangle pour lancer le jeu:
class Rect_run(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((140,40))
        self.image.fill(black)
        self.rect=self.image.get_rect()
        self.rect.center=(80, Y / 2 + 300)

    '''def b_run(self):
        global white, black, Y, menu_du_jeu, fontE
        self.brun = fontE.render('Lancer', True, white)
        menu_du_jeu.blit(brun, (25, Y / 2 + 305))
        return brun.get_rect()'''

#definition du rectangle pour acceder aux parametre:
class Rect_para(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((225,225))
        self.image.fill(black)
        self.rect=self.image.get_rect()
        self.rect.center=(250, 250)

    '''def b_run(self):
        menu_du_jeu.blit(brun, (25, Y / 2 + 305))
        return brun.get_rect()'''

#definition du sprite de la souris:
class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((4,4))
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.center=pygame.mouse.get_pos()

#definition de la Fenetre du menu:
class Fenetre:
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        #boucle while
    def run(self):
        global white, menu_du_jeu, titre, sous_titre, textRect, textRect2, mousse

        #variables appleant les class
        souris=Mouse()
        quitter = Rect_quit()
        run = Rect_run()
        para = Rect_para()

        #definition des sprites:
        allSprites=pygame.sprite.Group()
        allSprites.add(quitter)
        allSprites.add(run)
        allSprites.add(para)
        sourisSprites=pygame.sprite.Group(souris)
        
        #While True parceque les while True c'est toujours rigolo
        while True:
            #generation de la presentation du menu
            menu_du_jeu.fill(white)
            menu_du_jeu.blit(titre, textRect)
            menu_du_jeu.blit(sous_titre,textRect2)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    #bouton quitter
                    if  souris.rect.colliderect(quitter.rect):
                        pygame.quit()

                    #bouton lancer
                    elif souris.rect.colliderect(run.rect):
                        menu_du_jeu = pygame.display.set_mode((1050,800))
                        pygame.display.set_caption('Ecos')
                        game.run()

                    #bouton para
                    elif souris.rect.colliderect(run.rect):
                        menu_du_jeu = pygame.display.set_mode((640,480))
                        pygame.display.set_caption('Settings')
                        
            #mise a jour des sprites
            allSprites.update()
            sourisSprites.update()
            allSprites.draw(menu_du_jeu)
            pygame.display.flip()
        pygame.display.update()
            

fenetre=Fenetre().run()
