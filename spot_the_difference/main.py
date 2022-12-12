import logic
import validator
import display

board = logic.GameBoard(10)

display.Display.show(board.board)
print('間違いを見つけよう')

while True:
    
    coordinate = validator.GameValid.validate(input('入力例: A1\n'))

    if coordinate is False:
        print('入力しなおしてください')
        continue
    
    result = board.is_wrong_char(coordinate)

    if result is True:
        print('正解')
        break
    else:
        print('不正解')
