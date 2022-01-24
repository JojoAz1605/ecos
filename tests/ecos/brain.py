import time
from random import randint


class Brain:
    def __init__(self, owner):
        """Un cerveau pour une créature
        :param owner: le propriétaire du cerveau
        """
        self.owner = owner

    def idle(self):
        """Déplacement aléatoire"""
        nextMove = randint(0, 100)  # lance un dé virtuel, pour décider dans quelle direction aller

        if nextMove == 0:
            self.owner.move_left()
        elif nextMove == 1:
            self.owner.move_right()
        elif nextMove == 2:
            self.owner.move_up()
        elif nextMove == 3:
            self.owner.move_down()

    def doNextMove(self):
        """Choix du déplacement
        """
        self.idle()
