from player import Player


class Human(Player):

    def __init__(self, x, y, gender, name, health, attack, age, lifetime, grille):
        super().__init__(x, y, gender, name, health, attack, age, lifetime, grille)
        self.weapon = None

    def player_attack(self, target_player):
        damage = self.attack
        if self.has_weapon():
            damage += self.weapon.damage
        target_player.damage(damage)

    def set_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} a trouvé {self.weapon.name} et gagné {self.weapon.damage} points d'attaque")

    def has_weapon(self):
        return self.weapon is not None