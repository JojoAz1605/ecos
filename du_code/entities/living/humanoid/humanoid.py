from du_code.entities.living.livingentity import LivingEntity


class Humanoid(LivingEntity):
    def __init__(self, position, name, gender, grille):
        super().__init__(position, name, gender, grille)
        self.weapon = None
        self.eatable = ["rabbits", "wolves", "bears"]

    def entity_attack(self, target_player):
        damage = self.attack
        if self.has_weapon():
            damage += self.weapon.damage
        target_player.damage(damage)

    def set_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} a trouvé {self.weapon.name} et gagné {self.weapon.damage} points d'attaque")

    def has_weapon(self):
        return self.weapon is not None
