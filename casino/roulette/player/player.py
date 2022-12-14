from abstract_player import AbstractPlayer
from validator_for_player import validate

class Player(AbstractPlayer):
    def action(self):

        while True:
            place = validate(input('賭ける場所を入力してください：　'), self.__logic.bet_table)
            coin = validate(input('賭ける枚数を入力してください（１～所持枚数）：　'), range(1, self.__coin))
            
            if (place is False) or (coin is False):
                print('入力をやり直してください')
                continue
            else:
                break

    def bet(self):
        
        
        
