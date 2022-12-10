import random

class JankenLogic:
    def __init__(self, table):
        self.__table = table
    
    def is_winning(self, hand, opponent_hand):
        if self.__table[hand] is opponent_hand:
            return True
        elif self.__table[opponent_hand] is hand:
            return False
        else:
            return None

    def choice(self):
        return random.choice(list(self.__table.keys()))
        
