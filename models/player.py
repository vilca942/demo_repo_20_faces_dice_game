from models.dices import Dices


class Player:

    def __init__(self, player_name: str):
        self.name: str = player_name
        self.dices = Dices()
        self.dices_score: int = 0
        self.player_score: int = 0

    def get_name(self) -> str:
        return self.name

    def get_dices_score(self) -> int:
        return self.dices_score

    def get_player_score(self) -> int:
        return self.player_score

    def throw_dices(self):
        self.dices_score = self.dices.throw_dices()

    def player_wins_set(self):
        self.player_score += 1



