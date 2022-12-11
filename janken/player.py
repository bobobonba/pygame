class Player:
    def __init__(self, logic):
        self.__logic = logic
        self.__hand = None
    
    def action(self, hand = None):
        if hand is None:
            self.__hand = self.__logic.choice()
        else:
            self.__hand = hand

    def is_winning(self, opponent_hand):
        return self.__logic.is_winning(self.__hand, opponent_hand)

    @property
    def hand(self):
        return self.__hand