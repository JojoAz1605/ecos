from du_code.entities.living.livingentity import LivingEntity
import pygame


class Humanoid(LivingEntity):
    def __init__(self, position, name, gender, grille):
        super().__init__(position, name, gender, grille)
        self.weapon = None
        self.eatable = ["rabbits", "wolves", "bears"]
        self.recovery_time = 62
        self.age_mini = 16

    def check_equip_weapon(self) -> None:
        entity_group = self.world.entities["weapons"]
        if pygame.sprite.spritecollide(self, entity_group, False):
            for entity in entity_group:
                if not self.has_weapon() and entity.cooldown == 0 and self.rect.colliderect(entity):
                    self.set_weapon(entity)

    def entity_attack(self, target_player):
        if target_player is not None:
            damage = self.attack
            if self.has_weapon():
                damage += self.weapon.damage
            target_player.damage(damage)

    def checklist(self) -> None:
        self.check_pregnant()
        self.check_equip_weapon()
        self.check_attack()
        self.check_life()

    def set_weapon(self, weapon):
        weapon.cooldown = 365
        self.weapon = weapon
        print(f"\t{self.name} a trouvé {self.weapon.name} et gagne {self.weapon.damage} points d'attaque")

    def has_weapon(self):
        return self.weapon is not None
