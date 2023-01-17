from player_Parent import Player

class Game(Player):

    def __init__(self):
        pass
       

    def display_rules(self):
        print('Each match will be best of three games ')
        print('Rules: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. ')
 
    def run_game(self):
        print('Time to play Rock Paper Scissors Lizard Spock! ')

    def begin_round(self):
        return super().display_human_players()
        # self.begin_round = 1, 2
        # self.()

         

    def players_choose_gestures(self):
            self.begin_round = self.human_players 
print('please use number keys to choose selection')


n = input('Enter number:')


input('Rock crushes Scissors '[1])
input('Scissors cuts Paper' [2]) 
input('Paper covers Rock' [3])
input('Rock crushes Lizard' [4])
input('Lizard poisons Spock' [5])
input('Spock smashes Scissors' [6])
input('Scissors decapitates Lizard' [7])
input('Lizard eats Paper' [8])
input('Paper disproves Spock' [9])
input('Spock vaporizes Rock' [10])

print(input[int])
print([str])

    
                
            
        

        


#         For the Game class:
# What does the game need to have?
# 2 Players: 1 human, 1 AI
# What actions does the game need to perform?
# Display the game rules
# Determine 1 or 2 human players
# Have players choose gestures
# Compare the players' gestures to determine who wins the round/scores a point
# Display the winner, when the game is over