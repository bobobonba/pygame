from abc import ABCMeta, abstractmethod

class AbstractPlayer(metaclass = ABCMeta):
    def __init__(self, name, coin, game_instance):
        self._name = name
        self._coin = coin
        self._game = game_instance

        self._bet_place = None
        self._bet_coin = None

    def have_coin(self):
        if self._coin == 0:
            return False
        else:
            return True

    def get(self, coin):
        self._coin += coin
    
    def lost(self, coin):
        self._coin -= coin

    @abstractmethod
    def bet(self, coin=None, place=None):
        pass

    @property
    def name(self):
        return self._name

    @property
    def coin(self):
        return self._coin

    @property
    def bet_place(self):
        return self._bet_place
    
    @property
    def bet_coin(self):
        return self._bet_coin