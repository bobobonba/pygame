import random
import string

class GameBoard:
    PAIR = {"見": "貝"}

    def __init__(self, size):
        self.__size = size
        self.__collect_char = random.choice(list(GameBoard.PAIR.keys()))
        self.__board = self.create_board(self.__size, self.__collect_char)

        self.__x_coordinate = {char: index for index, char in enumerate(list(string.ascii_uppercase))}
        self.__y_coordinate = {i + 1: i for i in range(self.__size)}

        self.put_wrong_char()


    def create_board(self, size, char):
        return [[char for i in range(size)] for j in range(size)]

    def put_wrong_char(self):
        rand_x = random.randrange(self.__size)
        rand_y = random.randrange(self.__size)

        self.__board[rand_x][rand_y] = GameBoard.PAIR[self.__collect_char]
        self.__wrong_coordinate = str(rand_x) + str(rand_y)

    def is_wrong_char(self, coordinate_string):
        x, y  = list(coordinate_string)

        if self.__board[self.__x_coordinate[x]][self.__y_coordinate[int(y)]] == GameBoard.PAIR[self.__collect_char]:
            return True
        else:
            return False

    @property
    def board(self):
        return self.__board