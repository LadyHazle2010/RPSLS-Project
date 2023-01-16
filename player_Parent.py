
class Player:

    def __init__(self):
        self.number = 1,2
        self.human_players = True
 
       
      

    def display_human_players(self):
        self.number = input('Using number keys, Please choose between 1 or 2 players, How many players will be playing? ')
        if self.human_players is True:
            if self.number != [1, 2]:
                self.human_players = False
                print('Please choose between 1 or 2 players')

            else:
                self.human_players is False
                self.number == [1,2]
                self.human_players = True
                print('Great choice!' )
              

    def choose_gestures(self):
        

        
         print('please use number keys to choose selection')

    


