import logic
import player
import validator

table = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}
janken = logic.JankenLogic(table)

you = player.Player(janken)
opponent = player.Player(janken)

valid = validator.JankenValid(['グー', 'チョキ', 'パー'])

stream_count = 0 #連勝カウンタ
print('三連勝しよう')

while stream_count < 3:
    hand = valid.validate(input('\nグー チョキ パー\n'))

    #validateの結果がfalseだったら入力をしなおさせる
    if hand is False:
        print('グー　チョキ　パーの中から選んでね')
        continue


    you.action(hand)
    opponent.action()

    print('自分：', you.hand)
    print('相手：', opponent.hand)
    result = you.is_winning(opponent.hand)

    if result is None:
        print('あいこ')
        continue
    elif result is False:
        print('負け')
        stream_count = 0
    else:
        print('勝ち')
        stream_count += 1
        print('現在%s連勝目' % stream_count)

