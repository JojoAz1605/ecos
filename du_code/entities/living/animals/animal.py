from du_code.entities.living.livingentity import LivingEntity


class Animal(LivingEntity):
    def __init__(self, position, name, gender, grille):
        super().__init__(position, name, gender, grille)