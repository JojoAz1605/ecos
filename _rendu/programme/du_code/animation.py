import pygame


# Classe qui va gérer les animations
# class AnimateSprite(pygame.sprite.Sprite):

    # Définition des bases à la création de l'entité
    # def __init__(self, name):
        # super().__init__()
        # self.image = pygame.image.load(f'textures/entities/{name}.png')
        # self.current_image = 0  # Débuter à l'image 0
        # self.images = animations.get(name)

    # def animate(self):
        # self.current_image += 1  # Passer à l'image suivante
        # if self.current_image >= len(self.images):  # Vérifier si on arrive à la fin de l'animation
            # self.current_image = 0
        # self.image = self.images[self.current_image]


# Fonction pour charger les images
# def load_animation(name):
    # images = []  # Initialisation d'une liste vierge
    # Charger les 24 images du sprite
    # path = f'textures/entities/{name}'
    # for x in range(1, 24):
        # image_path = path + str(x) + ".png"
        # pygame.image.load(image_path)  # Ajout de chaque image à la liste images
    # return images  # Renvoi le contenu de la liste images


# Création d'un dictionnaire contenant les animations
# animations = {
    # 'human': load_animation("human")
    # 'orc' : load_animation("orc")
# }