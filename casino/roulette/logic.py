import random

class RouletteGame:
    MIN = 1
    MAX = 8
    RED = 'R'
    BLACK = 'B'

    def __init__(self):
        self.__bet_table = [self.RED, self.BLACK, '1', '2', '3', '4', '5', '6', '7', '8']

    def spin(self):
        return random.randrange(self.MIN, self.MAX + 1)
    
    def evaluate(self, number, bet_place):
        if (bet_place == self.RED) and (number % 2 == 1):
            return True
        elif (bet_place == self.BLACK) and (number % 2 == 0):
            return True
        elif number == bet_place:
            return True
        else:
            return False

    def calcu(self, place, coin):
        if (place == self.RED) or (place == self.BLACK):
            return int(coin) * 8
        else:
            return int(coin) * 2

    @property
    def bet_table(self):
        return self.__bet_table
