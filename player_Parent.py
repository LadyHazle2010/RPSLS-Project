
class Player:

    def __init__(self):
        self.number = 5
        self.human_players = True
 
       
      

    def display_human_players(self):
        self.human_players = input('Using number keys, Please choose between 2-5 players, How many players will be playing? ')
        while self.human_players is True:
            if self.number <= 5:
                 print('Great choice! ')
        else:
            self.human_players = False
            print('Please choose between 2-5 players.')
       
      


    # def choose_gestures(self):
            # print('please use number keys to choose gesture selection')
            # self.human_players = input(' Rock crushes Scissors' [1])



    


