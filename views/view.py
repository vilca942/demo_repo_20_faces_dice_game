class View:

    def __init__(self):
        pass

    def prompt_player_enter_game(self) -> str:
        return input("Entrer votre nom pour entrer dans la partie ou appuyer sur entrée pour lancer la partie : ")

    def prompt_launch_next_game(self):
        input("Pour lancer la prochaine manche appuyer sur entrée :")
