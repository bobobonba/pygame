from abc import ABCMeta

class AbstractPlayer(metaclass = ABCMeta):
    def __init__(self, coin_num, name, logic):
        self.__coin = coin_num
        self.__name = name
        self.__logic = logic

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def bet(self):
        pass

    def have_coin(self):
        return self.__coin

    
    @property
    def name(self):
        return self.__name

        