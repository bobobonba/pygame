import random
import string

class GameBoard:
    PAIR = {"見": "貝"}

    def __init__(self, size):
        self.__size = size
        self.__collect_char = random.choice(list(self.PAIR.keys()))
        self.__board = self.create_board(self.__size, self.__collect_char)

        self.__x_coordinate = {char: index for index, char in enumerate(list(string.ascii_uppercase))}
        self.__y_coordinate = {i: i + 1 for i in range(self.__size)}


    def create_board(size, char):
        return [[char for i in range(size)] for j in range(size)]

    def put_wrong_char(self):
        rand_x = random.randrange(self.__size)
        rand_y = random.randrange(self.__size)

        self.__board[rand_x][rand_y] = self.PAIR[self.__collect_char]

    def is_wrong_char(self, coordinate_string):
        x, y  = list(coordinate_string)

        if self.__board[self.__x_coordinate[x]][self.__y_coordinate[y]] == self.PAIR[self.__collect_char]:
            return False
        else:
            return True

    @property
    def board(self):
        return self.__board