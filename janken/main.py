import logic
import player

table = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}
janken = logic.JankenLogic(table)

you = player.Player(janken)
opponent = player.Player(janken)


stream_count = 0 #連勝カウンタ
print('三連勝しよう')

while stream_count < 3:
    hand = input('グー　チョキ　パー\n')

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
