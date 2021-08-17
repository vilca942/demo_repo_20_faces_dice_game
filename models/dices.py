from random import randint


class Dice:
    FACE_NUMBER = 20

    def __init__(self):
        pass

    def throw_dice(self) -> int:
        return randint(1, Dice.FACE_NUMBER)


class Dices:

    def __init__(self):
        self.dice_list = [Dice(), Dice()]

    def throw_dices(self) -> int:
        score = 0
        for dice in self.dice_list:
            score += dice.throw_dice()
        return score
