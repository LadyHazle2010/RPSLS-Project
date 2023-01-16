from player_Parent import Player

class Human(Player):

    def __init__(self) -> None:
        self.human_players = 1,2

    def human_players(self):
            self.human_players = input('Using number keys, Please choose between 2-5 players, How many players will be playing? ')
            print(input)

           