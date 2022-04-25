import pygame

# Classe qui va gérer les animations
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{name}.png')