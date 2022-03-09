import pygame.sprite


class Item(pygame.sprite.Sprite):
    def __init__(self, position, name):
        super().__init__()
        self.type = "items"
        self.position = list(position)
        self.name = name

        self.image = pygame.image.load("textures/items/placeholder.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey([0, 0, 0])
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)

        self.oldposition = self.position.copy()

    def save_location(self):
        self.oldposition = self.position.copy()

    def get_name(self):
        return self.name

    def update(self):  # Récupère la position de base
        self.rect.midbottom = self.position
        self.feet.midbottom = self.rect.midbottom
