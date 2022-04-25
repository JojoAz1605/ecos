import pygame
from du_code.game import Game

# presentation et declaration:
pygame.init()
game = Game()
white = (255, 255, 255)
black = (0, 0, 0)
X = 500
Y = 700
menu_du_jeu = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Menu du Jeu')

# logo
img = pygame.image.load('textures/logo/ecos.png')
imgRect = img.get_rect()
imgRect.center = (X // 2, 80)

# creation des titres et sous:
fontE = pygame.font.SysFont('arial', 32)
# creation d'une police pour les boutons:
sfont = pygame.freetype.Font("polices/FreeSansBold.ttf", 25)
# creation de la souris:
mousse = pygame.mouse.get_pos()


# definition du rectangle pour quitter la menu:
class Rect_quit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((140, 40))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (X / 2 + 80, Y / 2 + 20)


# definition du rectangle pour lancer le jeu:
class Rect_run(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((140, 40))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (X / 2 - 100, Y / 2 + 20)


# definition du sprite de la souris:
class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 4))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


# definition de la Fenetre du menu:
class Fenetre:
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

        # boucle while

    def run(self):
        global white, menu_du_jeu, mousse

        # variables appleant les class
        souris = Mouse()
        quitter = Rect_quit()
        run = Rect_run()

        # definition des sprites:
        allSprites = pygame.sprite.Group()
        allSprites.add(quitter)
        allSprites.add(run)
        sourisSprites = pygame.sprite.Group(souris)

        # While True parceque les while True c'est toujours rigolo
        while True:
            # generation de la presentation du menu
            menu_du_jeu.fill(white)
            menu_du_jeu.blit(img, imgRect)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    # bouton quitter
                    if souris.rect.colliderect(quitter.rect):
                        pygame.quit()

                    # bouton lancer
                    elif souris.rect.colliderect(run.rect):
                        menu_du_jeu = pygame.display.set_mode((1050, 800))
                        pygame.display.set_caption('Ecos')
                        game.run()

            # mise a jour des sprites
            allSprites.update()
            sourisSprites.update()
            allSprites.draw(menu_du_jeu)
            sfont.render_to(menu_du_jeu, (110, Y / 2 + 10), "Lancer", (255, 255, 255))
            sfont.render_to(menu_du_jeu, (X / 2 + 40, Y / 2 + 10), "Quitter", (255, 255, 255))
            pygame.display.flip()
        pygame.display.update()
