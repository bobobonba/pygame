import string

class Display:
    X_COORDINATE = list(string.ascii_uppercase)
    @classmethod
    def show(cls, board):
        first_line = "\\ | %s" % " ".join(cls.X_COORDINATE[0:len(board)])
        second_line = "_ " * (len(board) + 2)

        for index, string in enumerate(board):
            if index == 0:
                print(first_line)
                print(second_line)

            print("%d |" % (int(index) + 1), " ".join(board[index]))


