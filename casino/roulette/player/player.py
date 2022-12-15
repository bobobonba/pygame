from .abstract_player import AbstractPlayer

class Player(AbstractPlayer):
    def bet(self, coin, place):
        self._bet_coin = int(coin)
        self._bet_place = place