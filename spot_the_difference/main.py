import logic
import validator
import display

board = logic.GameBoard(10)
valid = validator.GameValid()
displayer = display.Display()

displayer.show(board.board)
print('間違いを見つけよう')

while True:
    
    coordinate = valid.validate(input('入力例: A1'))

    if coordinate is False:
        print('入力しなおしてください')
        continue
    
    result = board.is_wrong_char(coordinate)

    if result is True:
        print('正解')
    else:
        print('不正解')
        continue
