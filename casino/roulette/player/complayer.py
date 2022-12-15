from .abstract_player import AbstractPlayer
import random

class COMPlayer(AbstractPlayer):
    def bet(self):
        self._bet_place = random.choice(self._game.bet_table)
        self._bet_coin = random.randrange(1, 99)
    