from models.player import Player
from views.view import View


class Controler:
    MINIMUM_POINTS = 10

    def __init__(self):
        self.players_list = []
        self.moderator: Player = Player("Le modérateur")
        self.view = View()

    def add_player(self, player_name: str):
        player = Player(player_name)
        self.players_list.append(player)
        print(player_name+" entre dans la partie.")

    def is_players_list_empty(self):
        if not self.players_list:
            raise Exception("Aucun joueur n'est prêt à jouer.")

    def all_players_throw_dices(self):
        self.is_players_list_empty()
        self.moderator.throw_dices()
        print('')
        print(self.moderator.get_name() + " a jeté ses dés et a obtenu " + str(self.moderator.get_dices_score())+'.')
        for player in self.players_list:
            player.throw_dices()
            print(player.get_name() + " a jeté ses dés et a obtenu " + str(player.get_dices_score())+'.')
        print("Tous les joueurs et le modérateur ont lancé leurs dés.")

    def what_player_wins_set(self):
        self.is_players_list_empty()
        moderator_dices_score = self.moderator.get_dices_score()
        for player in self.players_list:
            player_dices_score = player.get_dices_score()
            if player_dices_score > moderator_dices_score:
                player.player_wins_set()
                print(player.get_name() +
                      " marque 1 point avec " +
                      str(player_dices_score) +
                      " contre " +
                      str(moderator_dices_score)
                      + '.')

    def game_ends(self) -> bool:
        self.is_players_list_empty()
        for player in self.players_list:
            if player.get_player_score() >= Controler.MINIMUM_POINTS:
                print(player.get_name()+" a gagné le jeu avec "+str(player.get_player_score())+' points!')
                return True
        return False

    def run(self):
        view = self.view
        player_name = "player_name"

        while player_name != "":
            player_name = view.prompt_player_enter_game()
            if player_name != '':
                self.add_player(player_name)

        while not self.game_ends():
            self.view.prompt_launch_next_game()
            self.all_players_throw_dices()
            self.what_player_wins_set()
