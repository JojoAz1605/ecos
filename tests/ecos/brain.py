from random import randint


class Brain:
    def __init__(self, owner):
        """Un cerveau pour une créature
        :param owner: le propriétaire du cerveau
        """
        self.owner = owner

    def doNextMove(self):
        """Fais un déplacement, mais pour l'instant, c'est aléatoire
        """
        nextMove = randint(0, 3)  # lance un dé virtuel, pour décider dans quelle direction aller

        if nextMove == 0:
            self.owner.move_left()
        elif nextMove == 1:
            self.owner.move_right()
        elif nextMove == 2:
            self.owner.move_up()
        else:
            self.owner.move_down()
